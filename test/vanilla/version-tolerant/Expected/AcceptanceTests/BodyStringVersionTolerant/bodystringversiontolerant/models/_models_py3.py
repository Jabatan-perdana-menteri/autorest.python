# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class RefColorConstant(msrest.serialization.Model):
    """RefColorConstant.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar color_constant: Referenced Color Constant Description. Has constant value: "green-color".
    :vartype color_constant: str
    :param field1: Sample string.
    :type field1: str
    """

    _validation = {
        "color_constant": {"required": True, "constant": True},
    }

    _attribute_map = {
        "color_constant": {"key": "ColorConstant", "type": "str"},
        "field1": {"key": "field1", "type": "str"},
    }

    color_constant = "green-color"

    def __init__(self, *, field1: Optional[str] = None, **kwargs):
        super(RefColorConstant, self).__init__(**kwargs)
        self.field1 = field1
