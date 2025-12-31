from os import environ, getcwd
from os.path import abspath, exists
from sys import path

import pytest

import pyaqsapi.listfunctions as listfunctions
from pyaqsapi.helperfunctions import aqs_credentials


@pytest.fixture
def setuppyaqsapi(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repository or in the final package. local loads the AQS user
        # credentials for testing
        path.append(abspath("./dev"))
        import local

        (AQSuser, AQSkey) = local.setuppyaqsapitest()
        aqs_credentials(username=AQSuser, key=AQSkey)
    else:
        # get the credential information from environment variables if using
        # github actions
        AQSuser = environ.get("AQSuser")
        assert AQSuser is not None
        AQSkey = environ.get("AQSkey")
        assert AQSkey is not None
        aqs_credentials(username=AQSuser, key=AQSkey)


def test_aqs_isavailable(setuppyaqsapi):
    assert listfunctions.aqs_isavailable(return_header=True).get_status_code() == "200"


def test_aqs_knownissues(setuppyaqsapi):
    assert listfunctions.aqs_knownissues(return_header=True).get_status_code() == "200"


def test_counties_by_state(setuppyaqsapi):
    assert listfunctions.aqs_counties_by_state(stateFIPS="37", return_header=True).get_status_code() == "200"


def test_aqs_sites_by_county(setuppyaqsapi):
    assert listfunctions.aqs_sites_by_county(stateFIPS="15", countycode="001", return_header=True).get_status_code() == "200"


def test_aqs_classes(setuppyaqsapi):
    assert listfunctions.aqs_classes(return_header=True).get_status_code() == "200"


def test_aqs_parameters_by_class(setuppyaqsapi):
    assert listfunctions.aqs_parameters_by_class(parameterclass="CRITERIA", return_header=True).get_status_code() == "200"


def test_aqs_mas(setuppyaqsapi):
    assert listfunctions.aqs_mas(return_header=True).get_status_code() == "200"


def test_aqs_pqaos(setuppyaqsapi):
    assert listfunctions.aqs_pqaos(return_header=True).get_status_code() == "200"


def test_aqs_cbsas(setuppyaqsapi):
    assert listfunctions.aqs_cbsas(return_header=True).get_status_code() == "200"


def test_aqs_states(setuppyaqsapi):
    assert listfunctions.aqs_states(return_header=True).get_status_code() == "200"


def test_aqs_revisionhistory(setuppyaqsapi):
    assert listfunctions.aqs_revisionhistory(return_header=True).get_status_code() == "200"


def test_aqs_fields_by_service(setuppyaqsapi):
    assert listfunctions.aqs_fields_by_service(service="sampleData", return_header=True).get_status_code() == "200"


def test_aqs_sampledurations(setuppyaqsapi):
    assert listfunctions.aqs_sampledurations(return_header=True).get_status_code() == "200"
