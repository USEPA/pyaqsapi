# -*- coding: utf-8 -*-

import pytest
from datetime import date
import pyaqsapi.bybox as bybox
from pyaqsapi.helperfunctions import aqs_credentials
from os.path import exists, abspath
from os import environ, getcwd
from sys import path


@pytest.fixture
def setuppyaqsapi(autouse=True):
    if exists(".\\dev\\local.py"):
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


def test_sampledata_bybox(setuppyaqsapi):
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
        == 200
    )


def test_monitors_bybox(setuppyaqsapi):
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
        == 200
    )


def test_annualsummary_bybox(setuppyaqsapi):
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
        == 200
    )


def test_dailysummary_bybox(setuppyaqsapi):
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
        == 200
    )


def test_quarterlysummary_bybox(setuppyaqsapi):
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
        == 200
    )
