from os import environ, getcwd
from os.path import abspath, exists
from sys import path

import pytest

import pyaqsapi.metadatafunctions as metadatafunctions
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


def test_aqs_knownissues(setuppyaqsapi):
    assert metadatafunctions.aqs_knownissues(return_header=True).get_status_code() == "200"


def test_aqs_revisionhistory(setuppyaqsapi):
    assert metadatafunctions.aqs_revisionhistory(return_header=True).get_status_code() == "200"
