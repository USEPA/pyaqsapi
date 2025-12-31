"""pyaqsapi tests for functions imported from the bybox submodule"""

from datetime import date
from importlib import import_module
from os import environ, getcwd
from os.path import abspath, exists
from sys import path

import pytest

# from pyaqsapi import bybox
# from pyaqsapi.helperfunctions import aqs_credentials
bybox = import_module(name="..bybox", package="pyaqsapi.bybox")
# from pyaqsapi.helperfunctions import aqs_credentials
helperfunctions = import_module(name="..helperfunctions", package="pyaqsapi.helperfunctions")


@pytest.fixture
def setuppyaqsapi_bybox(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repository or in the final package. local loads the AQS user
        # credentials for testing
        path.append(abspath("./dev/"))
        import local

        (AQSuser, AQSkey) = local.setuppyaqsapitest()
        # aqs_credentials(username=AQSuser, key=AQSkey)
    else:
        # get the credential information from environment variables if using
        # github actions
        AQSuser = environ.get("AQSuser")
        assert AQSuser is not None
        AQSkey = environ.get("AQSkey")
        assert AQSkey is not None
    helperfunctions.aqs_credentials(username=AQSuser, key=AQSkey)


def test_sampledata_bybox(setuppyaqsapi_bybox):
    assert (
        bybox.sampledata(
            parameter="44201",
            bdate=date(year=2015, month=5, day=1),
            edate=date(year=2015, month=5, day=2),
            minlat="33.3",
            maxlat="33.6",
            minlon="-87.0",
            maxlon="-86.7",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_monitors_bybox(setuppyaqsapi_bybox):
    assert (
        bybox.monitors(
            parameter="44201",
            bdate=date(year=2015, month=5, day=1),
            edate=date(year=2017, month=5, day=2),
            minlat="33.3",
            maxlat="33.6",
            minlon="-87.0",
            maxlon="-86.7",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_annualsummary_bybox(setuppyaqsapi_bybox):
    assert (
        bybox.annualsummary(
            parameter="44201",
            bdate=date(year=2015, month=5, day=1),
            edate=date(year=2015, month=5, day=2),
            minlat="33.3",
            maxlat="33.6",
            minlon="-87.0",
            maxlon="-86.7",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_dailysummary_bybox(setuppyaqsapi_bybox):
    assert (
        bybox.dailysummary(
            parameter="44201",
            bdate=date(year=2015, month=5, day=1),
            edate=date(year=2015, month=5, day=2),
            minlat="33.3",
            maxlat="33.6",
            minlon="-87.0",
            maxlon="-86.7",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_quarterlysummary_bybox(setuppyaqsapi_bybox):
    assert (
        bybox.quarterlysummary(
            parameter="44201",
            bdate=date(year=2015, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            minlat="33.3",
            maxlat="33.6",
            minlon="-87.0",
            maxlon="-86.7",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )
