# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, TYPE_CHECKING, TypeVar, Generic, Union

from .base_model import BaseModel
from .parameter import ClientParameter, ConfigParameter
from .parameter_list import ClientGlobalParameterList, ConfigGlobalParameterList
from .imports import FileImport, ImportType, TypingSection
from .lro_operation import LROOperation

ParameterListType = TypeVar(
    "ParameterListType",
    bound=Union[ClientGlobalParameterList, ConfigGlobalParameterList]
)

if TYPE_CHECKING:
    from .code_model import CodeModel


class _ClientConfigBase(BaseModel, Generic[ParameterListType]):
    """A service client."""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        parameters: ParameterListType,
    ):
        super().__init__(yaml_data, code_model)
        self.parameters = parameters
        self.url: str = self.yaml_data["url"]

    @property
    def description(self) -> str:
        return self.yaml_data["description"]

    @property
    def name(self) -> str:
        return self.yaml_data["name"]

class Client(_ClientConfigBase[ClientGlobalParameterList]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        parameters: ClientGlobalParameterList
    ):
        super().__init__(yaml_data, code_model, parameters)

    def pipeline_class(self, async_mode: bool) -> str:
        if self.code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    @property
    def send_request_name(self) -> str:
        return "send_request" if self.code_model.options["show_send_request"] else "_send_request"

    @property
    def has_parameterized_host(self) -> bool:
        return not any(p for p in self.parameters if p.is_host)

    @property
    def filename(self) -> str:
        if (
            self.code_model.options["version_tolerant"]
            or self.code_model.options["low_level_client"]
        ):
            return "_client"
        return f"_{self.code_model.module_name}"

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = FileImport()

        file_import.add_submodule_import("msrest", "Serializer", ImportType.THIRDPARTY)
        file_import.add_submodule_import(
            "msrest", "Deserializer", ImportType.THIRDPARTY
        )
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if self.code_model.options["azure_arm"]:
            file_import.add_submodule_import(
                "azure.mgmt.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_submodule_import(
                "azure.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )

        for gp in self.parameters:
            file_import.merge(gp.imports())
        file_import.add_submodule_import(
            "._configuration",
            f"{self.code_model.client.name}Configuration",
            ImportType.LOCAL,
        )

        return file_import

    def imports(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        if async_mode:
            file_import.add_submodule_import("typing", "Awaitable", ImportType.STDLIB)
            file_import.add_submodule_import(
                "azure.core.rest",
                "AsyncHttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.rest",
                "HttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
            TypingSection.CONDITIONAL,
        )
        for og in self.code_model.operation_groups:
            file_import.add_submodule_import(
                f".{self.code_model.operations_folder_name}",
                og.class_name,
                ImportType.LOCAL,
            )

        if self.code_model.object_types and self.code_model.options["models_mode"]:
            path_to_models = ".." if async_mode else "."
            file_import.add_submodule_import(path_to_models, "models", ImportType.LOCAL)
        else:
            # in this case, we have client_models = {} in the service client, which needs a type annotation
            # this import will always be commented, so will always add it to the typing section
            file_import.add_submodule_import(
                "typing", "Dict", ImportType.STDLIB, TypingSection.TYPING
            )
        file_import.add_submodule_import("copy", "deepcopy", ImportType.STDLIB)
        return file_import

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        try:
            mixin_operation = next(
                og
                for og in self.code_model.operation_groups
                if og.is_mixin
            )
            file_import.add_submodule_import(
                "._operations_mixin", mixin_operation.class_name, ImportType.LOCAL
            )
        except StopIteration:
            pass
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Client":
        parameters = [ClientParameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            parameters=ClientGlobalParameterList(code_model, parameters),
        )


class Config(_ClientConfigBase[ConfigGlobalParameterList]):

    @property
    def description(self) -> str:
        return (
            f"Configuration for {self.yaml_data['name']}.\n\n."
            "Note that all parameters used to create this instance are saved as instance attributes."
        )

    @property
    def name(self) -> str:
        return f"{super().name}Configuration"

    def imports(self, async_mode: bool) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "azure.core.configuration", "Configuration", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "azure.core.pipeline", "policies", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if self.code_model.options["package_version"]:
            file_import.add_submodule_import(
                ".._version" if async_mode else "._version", "VERSION", ImportType.LOCAL
            )
        for gp in self.parameters:
            file_import.merge(gp.imports())
        if self.code_model.options["azure_arm"]:
            policy = (
                "AsyncARMChallengeAuthenticationPolicy"
                if async_mode
                else "ARMChallengeAuthenticationPolicy"
            )
            file_import.add_submodule_import(
                "azure.mgmt.core.policies", "ARMHttpLoggingPolicy", ImportType.AZURECORE
            )
            file_import.add_submodule_import(
                "azure.mgmt.core.policies", policy, ImportType.AZURECORE
            )
        return file_import


    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Config":
        parameters = [ConfigParameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            parameters=ConfigGlobalParameterList(code_model, parameters),
        )
