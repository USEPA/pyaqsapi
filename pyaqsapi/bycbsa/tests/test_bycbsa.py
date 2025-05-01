from datetime import date
from importlib import import_module
from os import environ
from os.path import abspath, exists
from sys import path
from warnings import warn

import pytest

# import pyaqsapi.bycbsa as bycbsa
bycbsa = import_module(name="..bycbsa", package="pyaqsapi.bycbsa")
# from pyaqsapi.helperfunctions import aqs_credentials
helperfunctions = import_module(
    name="..helperfunctions", package="pyaqsapi.helperfunctions"
)


@pytest.fixture
def setuppyaqsapi_bycbsa(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repostiory or in the final package. local loads the AQS user
        # credentials for testing
        path.append(abspath("./dev/"))
        try:
            import local
        except ImportError:
            warn(
                "unable to import ./dev/local.py in bycbsa/tests/setupaqsapi \
                 setuppyaqsapi fixture"
            )
        (AQSuser, AQSkey) = local.setuppyaqsapitest()
    else:
        # get the credential information from environment variables if using
        # github actions
        AQSuser = environ.get("AQSuser")
        assert AQSuser is not None
        AQSkey = environ.get("AQSkey")
        assert AQSkey is not None
    helperfunctions.aqs_credentials(username=AQSuser, key=AQSkey)


def test_monitors(setuppyaqsapi_bycbsa):
    assert (
        bycbsa.monitors(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_annualsummary(setuppyaqsapi_bycbsa):
    assert (
        bycbsa.annualsummary(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_dailysummary(setuppyaqsapi_bycbsa):
    assert (
        bycbsa.dailysummary(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_sampledata(setuppyaqsapi_bycbsa):
    assert (
        bycbsa.sampledata(
            parameter="42602",
            bdate=date(year=2015, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_quarterlysummary(setuppyaqsapi_bycbsa):
    assert (
        bycbsa.quarterlysummary(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )
