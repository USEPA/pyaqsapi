from os import environ, getcwd
from os.path import abspath, exists
from sys import path

import pytest
from pandas import DataFrame

import pyaqsapi.listfunctions as listfunctions
from pyaqsapi.helperfunctions import aqs_credentials


@pytest.fixture
def setuppyaqsapi(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repostiory or in the final package. local looads the AQS user
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


# none of the other test functions use aqsremove_header, so we create a unit
# test to make sure that
def test_aqs_removeheader(setuppyaqsapi):
    returnvalue = listfunctions.aqs_knownissues(return_header=False)
    assert isinstance(returnvalue, DataFrame)
