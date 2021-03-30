# coding=utf-8
# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from attr import make_class
from azure.core.exceptions import HttpResponseError

from bodystring import AutoRestSwaggerBATService
from bodystring.models import Colors, RefColorConstant
from bodystring._rest import *
import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    def _make_request(request):
        return base_make_request_json_response(client, request)
    return _make_request

def test_null(make_request):
    request = build_string_get_null_request()
    assert make_request(request).text == ''

    request = build_string_put_null_request(content=None)
    make_request(request)

def test_empty(make_request, make_request_json_response):
    request = build_string_get_empty_request()
    assert "" == make_request_json_response(request)
    # changing this behavior because of this pr being merged: https://github.com/Azure/autorest.testserver/pull/145/files
    request = build_string_put_empty_request(json="")
    make_request(request)

def test_mbcs(make_request, make_request_json_response):
    try:
        test_str = (
            "\xe5\x95\x8a\xe9\xbd\x84\xe4\xb8\x82\xe7\x8b\x9b\xe7\x8b"
            "\x9c\xef\xa7\xb1\xef\xa4\xac\xef\xa7\xb1\xef\xa8\x8c\xef"
            "\xa8\xa9\xcb\x8a\xe3\x80\x9e\xe3\x80\xa1\xef\xbf\xa4\xe2"
            "\x84\xa1\xe3\x88\xb1\xe2\x80\x90\xe3\x83\xbc\xef\xb9\xa1"
            "\xef\xb9\xa2\xef\xb9\xab\xe3\x80\x81\xe3\x80\x93\xe2\x85"
            "\xb0\xe2\x85\xb9\xe2\x92\x88\xe2\x82\xac\xe3\x88\xa0\xe3"
            "\x88\xa9\xe2\x85\xa0\xe2\x85\xab\xef\xbc\x81\xef\xbf\xa3"
            "\xe3\x81\x81\xe3\x82\x93\xe3\x82\xa1\xe3\x83\xb6\xce\x91"
            "\xef\xb8\xb4\xd0\x90\xd0\xaf\xd0\xb0\xd1\x8f\xc4\x81\xc9"
            "\xa1\xe3\x84\x85\xe3\x84\xa9\xe2\x94\x80\xe2\x95\x8b\xef"
            "\xb8\xb5\xef\xb9\x84\xef\xb8\xbb\xef\xb8\xb1\xef\xb8\xb3"
            "\xef\xb8\xb4\xe2\x85\xb0\xe2\x85\xb9\xc9\x91\xee\x9f\x87"
            "\xc9\xa1\xe3\x80\x87\xe3\x80\xbe\xe2\xbf\xbb\xe2\xba\x81"
            "\xee\xa1\x83\xe4\x9c\xa3\xee\xa1\xa4\xe2\x82\xac").decode('utf-8')

    except AttributeError:
        test_str = (
            b"\xe5\x95\x8a\xe9\xbd\x84\xe4\xb8\x82\xe7\x8b\x9b\xe7\x8b"
            b"\x9c\xef\xa7\xb1\xef\xa4\xac\xef\xa7\xb1\xef\xa8\x8c\xef"
            b"\xa8\xa9\xcb\x8a\xe3\x80\x9e\xe3\x80\xa1\xef\xbf\xa4\xe2"
            b"\x84\xa1\xe3\x88\xb1\xe2\x80\x90\xe3\x83\xbc\xef\xb9\xa1"
            b"\xef\xb9\xa2\xef\xb9\xab\xe3\x80\x81\xe3\x80\x93\xe2\x85"
            b"\xb0\xe2\x85\xb9\xe2\x92\x88\xe2\x82\xac\xe3\x88\xa0\xe3"
            b"\x88\xa9\xe2\x85\xa0\xe2\x85\xab\xef\xbc\x81\xef\xbf\xa3"
            b"\xe3\x81\x81\xe3\x82\x93\xe3\x82\xa1\xe3\x83\xb6\xce\x91"
            b"\xef\xb8\xb4\xd0\x90\xd0\xaf\xd0\xb0\xd1\x8f\xc4\x81\xc9"
            b"\xa1\xe3\x84\x85\xe3\x84\xa9\xe2\x94\x80\xe2\x95\x8b\xef"
            b"\xb8\xb5\xef\xb9\x84\xef\xb8\xbb\xef\xb8\xb1\xef\xb8\xb3"
            b"\xef\xb8\xb4\xe2\x85\xb0\xe2\x85\xb9\xc9\x91\xee\x9f\x87"
            b"\xc9\xa1\xe3\x80\x87\xe3\x80\xbe\xe2\xbf\xbb\xe2\xba\x81"
            b"\xee\xa1\x83\xe4\x9c\xa3\xee\xa1\xa4\xe2\x82\xac").decode('utf-8')

    request = build_string_get_mbcs_request()
    assert test_str == make_request_json_response(request)

    request = build_string_put_mbcs_request(content=test_str)
    make_request(request)

def test_whitespace(make_request, make_request_json_response):
    test_str = "    Now is the time for all good men to come to the aid of their country    "
    request = build_string_get_whitespace_request()
    assert test_str == make_request_json_response(request)

    request = build_string_put_whitespace_request(json=test_str)
    make_request(request)

def test_get_not_provided(make_request):
    request = build_string_get_not_provided_request()
    assert make_request(request).text == ''

def test_enum_not_expandable(make_request, make_request_json_response):
    request = build_enum_get_not_expandable_request()
    assert Colors.RED_COLOR == make_request_json_response(request)

    request = build_enum_put_not_expandable_request(json='red color')
    make_request(request)

    request = build_enum_put_not_expandable_request(json=Colors.RED_COLOR)
    make_request(request)
    # Autorest v3 is switching behavior here. Old Autorest would have thrown a serialization error,
    # but now we allow the user to pass strings as enums, so the raised exception is different.

    request = build_enum_put_not_expandable_request(json='not a color')
    with pytest.raises(HttpResponseError):
        make_request(request)

def test_get_base64_encdoded(make_request):
    request = build_string_get_base64_encoded_request()
    assert make_request(request).text.encode() ==  'a string that gets encoded with base64'.encode()

def test_base64_url_encoded(make_request, make_request_json_response):
    request = build_string_get_base64_url_encoded_request()
    assert make_request_json_response(request) ==  'a string that gets encoded with base64url'.encode()

    request = build_string_put_base64_url_encoded_request(content='a string that gets encoded with base64url'.encode())
    make_request(request)

def test_get_null_base64_url_encoded(make_request):
    request = build_string_get_null_base64_url_encoded_request()
    assert make_request(request).text == ''

def test_enum_referenced(make_request, make_request_json_response):
    request = build_enum_put_referenced_request(json=Colors.RED_COLOR)
    make_request(request)

    request = build_enum_put_referenced_request(json="red color")
    make_request(request)

    request = build_enum_get_referenced_request()
    assert make_request_json_response(request) == Colors.RED_COLOR

def test_enum_referenced_constant(make_request, make_request_json_response):
    request = build_enum_put_referenced_request(json=RefColorConstant().serialize())
    make_request(request)

    request = build_enum_get_referenced_constant_request()
    response = RefColorConstant.deserialize(make_request_json_response(request))
    assert response.color_constant ==  Colors.GREEN_COLOR.value
