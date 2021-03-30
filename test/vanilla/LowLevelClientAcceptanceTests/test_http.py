﻿# --------------------------------------------------------------------------
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

import requests

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import ContentDecodePolicy, RetryPolicy, HeadersPolicy, RedirectPolicy

from httpinfrastructure import AutoRestHttpInfrastructureTestService
from httpinfrastructure._rest import *

import pytest


@pytest.fixture()
def client(cookie_policy):
    """Create a AutoRestHttpInfrastructureTestService client with test server credentials."""
    policies = [
        HeadersPolicy(),
        ContentDecodePolicy(),
        RedirectPolicy(),
        RetryPolicy(),
        cookie_policy
    ]
    with AutoRestHttpInfrastructureTestService(base_url="http://localhost:3000", policies=policies) as client:
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

@pytest.fixture
def make_request_assert_status(client, base_make_request):
    def _make_request(request, status_code):
        response = base_make_request(client, request)
        assert response.status_code == status_code
    return _make_request

@pytest.fixture
def make_request_assert_raises_with_message(client, base_make_request):
    def _make_request(request, message):
        with pytest.raises(HttpResponseError) as ex:
            base_make_request(client, request)
        assert ex.value.message == message
    return _make_request

@pytest.fixture
def make_request_assert_raises_with_status(client, base_make_request):
    def _make_request(request, status_code):
        with pytest.raises(HttpResponseError) as ex:
            base_make_request(client, request)
        assert ex.value.status_code == status_code
    return _make_request

@pytest.fixture
def make_request_assert_raises_with_status_and_message(client, base_make_request):
    def _make_request(request, status_code, message):
        with pytest.raises(HttpResponseError) as ex:
            base_make_request(client, request)
        assert ex.value.status_code == status_code
        assert ex.value.message == message
        assert message in str(ex.value)
    return _make_request

@pytest.fixture
def make_request_assert_raises_with_status_and_response_contains_message(client, base_make_request):
    def _make_request(request, status_code, message):
        with pytest.raises(HttpResponseError) as ex:
            base_make_request(client, request)
        assert ex.value.status_code == status_code
        assert message in str(ex.value)
    return _make_request

def test_get200_model204(make_request, make_request_assert_status, make_request_assert_raises_with_status_and_response_contains_message):
    # a lot of these tests raised in high level bc we made some 200 status codes errors in high level
    # can't do this in low level, so these don't actually raise
    request = build_multipleresponses_get200_model204_no_model_default_error200_valid_request()
    make_request_assert_status(request, 200)

    request = build_multipleresponses_get200_model204_no_model_default_error201_invalid_request()
    make_request_assert_status(request, 201)

    request = build_multipleresponses_get200_model204_no_model_default_error202_none_request()
    make_request_assert_status(request, 202)

    request = build_multipleresponses_get200_model204_no_model_default_error204_valid_request()

    assert make_request(request).text == ''

    request = build_multipleresponses_get200_model204_no_model_default_error400_valid_request()
    make_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

def test_get200_model201(make_request_json_response, make_request_assert_status, make_request_assert_raises_with_status_and_response_contains_message):
    request = build_multipleresponses_get200_model201_model_default_error200_valid_request()
    make_request_assert_status(request, 200)

    request = build_multipleresponses_get200_model201_model_default_error201_valid_request()
    b_model = make_request_json_response(request)
    assert b_model is not None
    assert b_model['statusCode'] ==  "201"
    assert b_model['textStatusCode'] ==  "Created"

    request = build_multipleresponses_get200_model201_model_default_error400_valid_request()
    make_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

def test_get200_model_a201_model_c404(make_request_json_response, make_request_assert_raises_with_status_and_response_contains_message, make_request_assert_raises_with_status):
    request = build_multipleresponses_get200_model_a201_model_c404_model_d_default_error200_valid_request()
    a_model = make_request_json_response(request)
    assert a_model['statusCode']==  "200"

    request = build_multipleresponses_get200_model_a201_model_c404_model_d_default_error201_valid_request()

    c_model = make_request_json_response(request)
    assert c_model['httpCode'] ==  "201"

    request = build_multipleresponses_get200_model_a201_model_c404_model_d_default_error404_valid_request()
    make_request_assert_raises_with_status(request, 404)  # in high level, this doesn't raise and returns a model since we've made 404 a valid status code. can't do that in llc

    request = build_multipleresponses_get200_model_a201_model_c404_model_d_default_error400_valid_request()
    make_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

def test_get202_none204(make_request, make_request_assert_raises_with_status, make_request_assert_raises_with_status_and_response_contains_message):
    request = build_multipleresponses_get202_none204_none_default_error202_none_request()
    make_request(request)

    request = build_multipleresponses_get202_none204_none_default_error204_none_request()
    make_request(request)

    request = build_multipleresponses_get202_none204_none_default_error400_valid_request()
    make_request_assert_raises_with_status_and_response_contains_message(request, 400, "client error")

    request = build_multipleresponses_get202_none204_none_default_none202_invalid_request()
    make_request(request)

    request = build_multipleresponses_get202_none204_none_default_none204_none_request()
    make_request(request)

    request = build_multipleresponses_get202_none204_none_default_none400_none_request()
    make_request_assert_raises_with_status(request, 400)

    request = build_multipleresponses_get202_none204_none_default_none400_invalid_request()
    make_request_assert_raises_with_status(request, 400)

def test_get_default_model_a200(make_request, make_request_assert_status):
    request = build_multipleresponses_get_default_model_a200_valid_request()
    make_request_assert_status(request, 200)

    request = build_multipleresponses_get_default_model_a200_none_request()
    assert make_request(request).text == ''

    request = build_multipleresponses_get_default_model_a200_valid_request()
    make_request(request)
    request = build_multipleresponses_get_default_model_a200_none_request()
    make_request(request)

def test_get_default_none200(make_request):
    request = build_multipleresponses_get_default_none200_invalid_request()
    make_request(request)

    requst = build_multipleresponses_get_default_none200_none_request()
    make_request(request)

def test_get_default_none400(make_request_assert_raises_with_status):
    request = build_multipleresponses_get_default_none400_invalid_request()
    make_request_assert_raises_with_status(request, 400)

    request = build_multipleresponses_get_default_none400_none_request()
    make_request_assert_raises_with_status(request, 400)

def test_get200_model_a200(make_request, make_request_assert_status):
    request = build_multipleresponses_get200_model_a200_none_request()
    assert make_request(request).text == ''

    request = build_multipleresponses_get200_model_a200_valid_request()
    make_request_assert_status(request, 200)

    request = build_multipleresponses_get200_model_a200_invalid_request()
    make_request_assert_status(request, 200) # in high level it's supposed to deserialize as exception model "MyException", can't do that in LLC

def test_get200_model_a400(make_request_assert_raises_with_status):
    request = build_multipleresponses_get200_model_a400_none_request()
    make_request_assert_raises_with_status(request, 400)

    request = build_multipleresponses_get200_model_a400_valid_request()
    make_request_assert_raises_with_status(request, 400)

    request = build_multipleresponses_get200_model_a400_invalid_request()
    make_request_assert_raises_with_status(request, 400)

def test_get200_model_a202(make_request_assert_status):
    request = build_multipleresponses_get200_model_a202_valid_request()
    make_request_assert_status(request, 202)  # raises in HLC bc we've marked all status codes that are not "200" as errors

def test_server_error_status_codes_501(make_request_assert_raises_with_status):
    request = build_httpserverfailure_head501_request()
    make_request_assert_raises_with_status(request, requests.codes.not_implemented)

    request = build_httpserverfailure_get501_request()
    make_request_assert_raises_with_status(request, requests.codes.not_implemented)

def test_server_error_status_codes_505(make_request_assert_raises_with_status):
    request = build_httpserverfailure_post505_request()
    make_request_assert_raises_with_status(request, requests.codes.http_version_not_supported)

    request = build_httpserverfailure_delete505_request()
    make_request_assert_raises_with_status(request, requests.codes.http_version_not_supported)

def test_retry_status_codes_408(make_request):
    request = build_httpretry_head408_request()
    make_request(request)

def test_retry_status_codes_502(make_request):
    request = build_httpretry_get502_request()
    make_request(request)

    # TODO, 4042586: Support options operations in swagger modeler
    #client.http_retry.options429()

def test_retry_status_codes_500(make_request):
    request = build_httpretry_put500_request()
    make_request(request)
    request = build_httpretry_patch500_request()
    make_request(request)

def test_retry_status_codes_503(make_request):
    request = build_httpretry_post503_request()
    make_request(request)

    request = build_httpretry_delete503_request()
    make_request(request)

def test_retry_status_codes_504(make_request):
    request = build_httpretry_put504_request()
    make_request(request)

    request = build_httpretry_patch504_request()
    make_request(request)

def test_error_status_codes_400(make_request_assert_raises_with_status):
    request = build_httpclientfailure_head400_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = build_httpclientfailure_get400_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)

    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_raises_with_status(requests.codes.bad_request,
    #    client.http_client_failure.options400)

    request = build_httpclientfailure_put400_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = build_httpclientfailure_patch400_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = build_httpclientfailure_post400_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)

    request = build_httpclientfailure_delete400_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)

def test_error_status_codes_401(make_request_assert_raises_with_status):
    request = build_httpclientfailure_head401_request()
    make_request_assert_raises_with_status(request, requests.codes.unauthorized)

def test_error_status_codes_402(make_request_assert_raises_with_status):
    request = build_httpclientfailure_get402_request()
    make_request_assert_raises_with_status(request, requests.codes.payment_required)

def test_error_status_codes_403(make_request_assert_raises_with_status):
    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_raises_with_status(requests.codes.forbidden,
    #    client.http_client_failure.options403)

    request = build_httpclientfailure_get403_request()
    make_request_assert_raises_with_status(request, requests.codes.forbidden)

def test_error_status_codes_404(make_request_assert_raises_with_status):
    request = build_httpclientfailure_put404_request()
    make_request_assert_raises_with_status(request, requests.codes.not_found)

def test_error_status_codes_405(make_request_assert_raises_with_status):
    request = build_httpclientfailure_patch405_request()
    make_request_assert_raises_with_status(request, requests.codes.method_not_allowed)

def test_error_status_codes_406(make_request_assert_raises_with_status):
    request = build_httpclientfailure_post406_request()
    make_request_assert_raises_with_status(request, requests.codes.not_acceptable)

def test_error_status_codes_407(make_request_assert_raises_with_status):
    request = build_httpclientfailure_delete407_request()
    make_request_assert_raises_with_status(request, requests.codes.proxy_authentication_required)

def test_error_status_codes_409(make_request_assert_raises_with_status):
    request = build_httpclientfailure_put409_request()
    make_request_assert_raises_with_status(request, requests.codes.conflict)

def test_error_status_codes_410(make_request_assert_raises_with_status):
    request = build_httpclientfailure_head410_request()
    make_request_assert_raises_with_status(request, requests.codes.gone)

def test_error_status_codes_411(make_request_assert_raises_with_status):

    request = build_httpclientfailure_get411_request()
    make_request_assert_raises_with_status(request, requests.codes.length_required)

    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_raises_with_status(requests.codes.precondition_failed,
    #    client.http_client_failure.options412)

    request = build_httpclientfailure_get412_request()
    make_request_assert_raises_with_status(request, requests.codes.precondition_failed)

    request = build_httpclientfailure_put413_request()
    make_request_assert_raises_with_status(request, requests.codes.request_entity_too_large)

    request = build_httpclientfailure_patch414_request()
    make_request_assert_raises_with_status(request, requests.codes.request_uri_too_large)

    request = build_httpclientfailure_post415_request()
    make_request_assert_raises_with_status(request, requests.codes.unsupported_media)

    request = build_httpclientfailure_get416_request()
    make_request_assert_raises_with_status(request, requests.codes.requested_range_not_satisfiable)

    request = build_httpclientfailure_delete417_request()
    make_request_assert_raises_with_status(request, requests.codes.expectation_failed)

    request = build_httpclientfailure_head429_request()
    make_request_assert_raises_with_status(request, 429)

def test_redirect_to_300(make_request_assert_status):
    request = build_httpredirects_get300_request()
    make_request_assert_status(request, 200)

def test_redirect_to_301(make_request_assert_status):
    request = build_httpredirects_head301_request()
    make_request_assert_status(request, 200)


    request = build_httpredirects_get301_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_put301_request()
    make_request_assert_status(request, requests.codes.moved_permanently)

def test_redirect_to_302(make_request_assert_status):
    request = build_httpredirects_head302_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_get302_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_patch302_request()
    make_request_assert_status(request, requests.codes.found)

def test_redicret_to_303(make_request_assert_status):
    request = build_httpredirects_post303_request()
    make_request_assert_status(request, 200)

def test_redirect_to_307(make_request_assert_status):
    request = build_httpredirects_head307_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_get307_request()
    make_request_assert_status(request, 200)

    # TODO, 4042586: Support options operations in swagger modeler
    #self.assert_status(200, client.http_redirects.options307)
    request = build_httpredirects_put307_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_post307_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_patch307_request()
    make_request_assert_status(request, 200)

    request = build_httpredirects_delete307_request()
    make_request_assert_status(request, 200)

def test_bad_request_status_assert(make_request_assert_raises_with_message):
    request = build_httpfailure_get_empty_error_request()
    make_request_assert_raises_with_message(request, "Operation returned an invalid status 'Bad Request'")

def test_no_error_model_status_assert(make_request_assert_raises_with_status_and_response_contains_message):
    request = build_httpfailure_get_no_model_error_request()
    make_request_assert_raises_with_status_and_response_contains_message(request, requests.codes.bad_request, "NoErrorModel")

def test_success_status_codes_200(make_request):
    request = build_httpsuccess_head200_request()
    make_request(request)
    request = build_httpsuccess_get200_request()
    assert make_request(request).text

    request = build_httpsuccess_put200_request()
    make_request(request)

    request = build_httpsuccess_post200_request()
    make_request(request)

    request = build_httpsuccess_patch200_request()
    make_request(request)

    request = build_httpsuccess_delete200_request()
    make_request(request)

    # TODO, 4042586: Support options operations in swagger modeler
    #assert client.http_success.options200()

def test_success_status_codes_201(make_request):
    request = build_httpsuccess_put201_request()
    make_request(request)

    request = build_httpsuccess_post201_request()
    make_request(request)

def test_success_status_codes_202(make_request):
    request = build_httpsuccess_put202_request()
    make_request(request)

    request = build_httpsuccess_post202_request()
    make_request(request)

    request = build_httpsuccess_patch202_request()
    make_request(request)

    request = build_httpsuccess_delete202_request()
    make_request(request)

def test_success_status_codes_204(make_request):
    request = build_httpsuccess_head204_request()
    make_request(request)

    request = build_httpsuccess_put204_request()
    make_request(request)

    request = build_httpsuccess_post204_request()
    make_request(request)

    request = build_httpsuccess_delete204_request()
    make_request(request)

    request = build_httpsuccess_patch204_request()
    make_request(request)

def test_success_status_codes_404(make_request_assert_raises_with_status):
    # raises bc in high level we're able to mark 404 as a valid status code, but can't do that in llc
    request = build_httpsuccess_head404_request()
    make_request_assert_raises_with_status(request, 404)

def test_empty_no_content(make_request_assert_raises_with_status):
    request = build_httpfailure_get_no_model_empty_request()
    make_request_assert_raises_with_status(request, requests.codes.bad_request)
