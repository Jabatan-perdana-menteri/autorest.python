# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, List, Any, Optional, Union, TYPE_CHECKING

from .operation import Operation
from .response import Response
from .request_builder import OverloadedRequestBuilder, RequestBuilder, RequestBuilderBase
from .imports import ImportType, FileImport, TypingSection
from .parameter_list import ParameterList

if TYPE_CHECKING:
    from .code_model import CodeModel

class PagingOperation(Operation):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        request_builder: RequestBuilder,
        parameters: ParameterList,
        responses: List[Response],
        *,
        overloads: Optional[List[Operation]] = None,
        public: bool = True,
        want_tracing: bool = True,
        abstract: bool = False,
        override_success_response_to_200: bool = False,
    ) -> None:
        super().__init__(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            request_builder=request_builder,
            parameters=parameters,
            responses=responses,
            overloads=overloads,
            public=public,
            want_tracing=want_tracing,
            abstract=abstract,
        )
        self.next_request_builder: Optional[Union[RequestBuilder, OverloadedRequestBuilder]] = RequestBuilderBase.from_yaml(
            self.yaml_data["nextOperation"], code_model) if self.yaml_data.get("nextOperation"
        ) else None
        self.item_name: str = self.yaml_data["itemName"]
        self.continuation_token_name: str = self.yaml_data["continuationTokenName"]
        self.override_success_response_to_200 = override_success_response_to_200
        self.pager_sync: str = yaml_data["pagerSync"]
        self.pager_async: str = yaml_data["pagerAsync"]
        self.operation_type = "paging"

    def get_pager_path(self, async_mode: bool) -> str:
        return self.yaml_data["pagerAsync"] if async_mode else self.yaml_data["pagerSync"]

    def get_pager(self, async_mode: bool) -> str:
        return self.get_pager_path(async_mode).split(".")[-1]

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{super().response_type_annotation(async_mode=async_mode)}]"

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = super()._imports_shared(async_mode)
        if async_mode:
            file_import.add_submodule_import(
                "typing", "AsyncIterable", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        else:
            file_import.add_submodule_import(
                "typing", "Iterable", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        if (
            self.next_request_builder
            and self.code_model.options["builders_visibility"] == "embedded"
            and not async_mode
        ):
            file_import.merge(self.next_request_builder.imports())
        return file_import

    @property
    def has_optional_return_type(self) -> bool:
        return False

    def response_type_annotation(self, *, async_mode: bool, **kwargs) -> str:
        iterable = "AsyncIterable" if async_mode else "Iterable"
        return f"{iterable}[{super().response_type_annotation(async_mode=async_mode)}]"

    def response_docstring_type(self, *, async_mode: bool, **kwargs) -> str:
        return f"~{self.get_pager_path(async_mode)}[{super().response_docstring_type(async_mode=async_mode)}]"

    def response_docstring_text(self, *, async_mode: bool, **kwargs) -> str:
        super_text = super().response_docstring_text(async_mode=async_mode)
        base_description = "An iterator like instance of "
        if not self.code_model.options["version_tolerant"]:
            base_description += "either "
        return base_description + super_text

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = super().imports_for_multiapi(async_mode)
        pager_import_path = ".".join(self.get_pager_path(async_mode).split(".")[:-1])
        pager = self.get_pager(async_mode)

        file_import.add_submodule_import(
            pager_import_path, pager, ImportType.AZURECORE, TypingSection.CONDITIONAL
        )

        return file_import

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_base(async_mode, is_python3_file)
        # operation adds an import for distributed_trace_async, we don't want it
        file_import.imports = [
            i
            for i in file_import.imports
            if not i.submodule_name == "distributed_trace_async"
        ]

        pager_import_path = ".".join(self.get_pager_path(async_mode).split(".")[:-1])
        pager = self.get_pager(async_mode)

        file_import.add_submodule_import(pager_import_path, pager, ImportType.AZURECORE)

        if async_mode:
            file_import.add_submodule_import(
                "azure.core.async_paging", "AsyncList", ImportType.AZURECORE
            )

        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                "azure.core.tracing.decorator",
                "distributed_trace",
                ImportType.AZURECORE,
            )
        if self.next_request_builder:
            file_import.merge(self.get_request_builder_import(self.next_request_builder, async_mode))

        return file_import
