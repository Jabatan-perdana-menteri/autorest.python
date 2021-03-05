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

    :param code:
    :type code: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[int] = None, message: Optional[str] = None, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message


class SampleResourceGroup(msrest.serialization.Model):
    """SampleResourceGroup.

    :param name: resource group name 'testgroup101'.
    :type name: str
    :param location: resource group location 'West US'.
    :type location: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None, location: Optional[str] = None, **kwargs):
        super(SampleResourceGroup, self).__init__(**kwargs)
        self.name = name
        self.location = location
