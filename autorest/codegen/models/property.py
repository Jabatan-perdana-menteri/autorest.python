# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TYPE_CHECKING

from .base_model import BaseModel
from .constant_type import ConstantType
from .base_type import BaseType
from .imports import FileImport
from .utils import add_to_description

if TYPE_CHECKING:
    from .code_model import CodeModel


class Property(BaseModel):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.rest_api_name = self.yaml_data["restApiName"]
        self.client_name = self.yaml_data["clientName"]
        self.type = type
        self.optional: bool = self.yaml_data["optional"]
        self.readonly: bool = self.yaml_data.get("readonly", False)
        self.is_discriminator: bool = yaml_data.get("isDiscriminator", False)
        self.client_default_value = yaml_data.get("clientDefaultValue", None)

    def description(self, *, is_operation_file: bool) -> str:
        description = self.yaml_data["description"]
        return add_to_description(description, self.type.description(is_operation_file=is_operation_file))

    @property
    def constant(self) -> bool:
        # this bool doesn't consider you to be constant if you are a discriminator
        # you also have to be required to be considered a constant
        return (
            isinstance(self.type, ConstantType)
            and not self.optional
            and not self.is_discriminator
        )

    @property
    def is_input(self):
        return not (self.constant or self.readonly or self.is_discriminator)

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if self.optional:
            return f"Optional[{self.type.type_annotation(is_operation_file=is_operation_file)}]"
        return self.type.type_annotation(is_operation_file=is_operation_file)

    def get_json_template_representation(self, *, optional: bool = True, client_default_value_declaration: Optional[str] = None, description: Optional[str] = None) -> Any:
        if self.client_default_value:
            client_default_value_declaration = self.type.get_declaration(self.client_default_value)
        if self.description(is_operation_file=True):
            description = self.description(is_operation_file=True)
        return self.type.get_json_template_representation(optional=self.optional, client_default_value_declaration=client_default_value_declaration, description=description)

    @property
    def validation(self) -> Optional[Dict[str, Any]]:
        retval: Dict[str, Any] = {}
        if not self.optional:
            retval["required"] = True
        if self.readonly:
            retval["readonly"] = True
        if self.constant:
            retval["constant"] = True
        retval.update(self.type.validation or {})
        return retval or None

    @property
    def attribute_map(self) -> str:
        return f'"{self.client_name}": {{"key": "{self.rest_api_name}", "type": "{self.serialization_type}"}},'

    def imports(self) -> FileImport:
        return self.type.imports(is_operation_file=False)

    @classmethod
    def from_yaml(
        cls,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
    ) -> "Property":
        from . import build_type  # pylint: disable=import-outside-toplevel
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=build_type(yaml_data["type"], code_model)
        )
