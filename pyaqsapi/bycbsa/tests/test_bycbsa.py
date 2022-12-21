# -*- coding: utf-8 -*-

import pytest
from datetime import date
import pyaqsapi.bycbsa as bycbsa
from pyaqsapi.helperfunctions import aqs_credentials
from os.path import exists, abspath
from os import environ, getcwd
from sys import path


@pytest.fixture
def setuppyaqsapi(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repostiory or in the final package. local looads the AQS user
        # credentials for testing
        path.append(abspath("./dev"))
        import local

        AQSuser, AQSkey = local.setuppyaqsapitest()
        aqs_credentials(username=AQSuser, key=AQSkey)
    else:
        # get the credential information from environment variables if using
        # github actions
        AQSuser = environ.get("AQSuser")
        assert AQSuser is not None
        AQSkey = environ.get("AQSkey")
        assert AQSkey is not None
        aqs_credentials(username=AQSuser, key=AQSkey)


def test_monitors(setuppyaqsapi):
    assert (
        bycbsa.monitors(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_annualsummary(setuppyaqsapi):
    assert (
        bycbsa.annualsummary(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_dailysummary(setuppyaqsapi):
    assert (
        bycbsa.dailysummary(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_sampledata(setuppyaqsapi):
    assert (
        bycbsa.sampledata(
            parameter="42602",
            bdate=date(year=2015, month=1, day=1),
            edate=date(year=2017, month=1, day=1),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_quarterlysummary(setuppyaqsapi):
    assert (
        bycbsa.quarterlysummary(
            parameter="42602",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            cbsa_code="16740",
            return_header=True,
        )[0].get_status_code()
        == 200
    )
