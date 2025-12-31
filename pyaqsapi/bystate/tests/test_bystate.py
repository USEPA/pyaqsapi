"""pyaqsapi tests for functions imported from the bystate submodule"""

from datetime import date
from os import environ
from os.path import abspath, exists
from sys import path

import pytest

import pyaqsapi.bystate as bystate
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


def test_monitors(setuppyaqsapi):
    assert (
        bystate.monitors(
            parameter="88101",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_sampledata(setuppyaqsapi):
    assert (
        bystate.sampledata(
            parameter="45201",
            bdate=date(year=1995, month=5, day=15),
            edate=date(year=1995, month=5, day=15),
            stateFIPS="37",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_annualsummary(setuppyaqsapi):
    assert (
        bystate.annualsummary(
            parameter="45201",
            bdate=date(year=1995, month=5, day=15),
            edate=date(year=1999, month=5, day=15),
            stateFIPS="37",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_dailysummary(setuppyaqsapi):
    assert (
        bystate.dailysummary(
            parameter="45201",
            bdate=date(year=1995, month=5, day=15),
            edate=date(year=1995, month=5, day=15),
            stateFIPS="37",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_blanks(setuppyaqsapi):
    assert (
        bystate.qa_blanks(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_collocated_assessments(setuppyaqsapi):
    assert (
        bystate.qa_collocated_assessments(
            parameter="88101",
            bdate=date(year=2013, month=1, day=1),
            edate=date(year=2013, month=1, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_flowrateaudit(setuppyaqsapi):
    assert (
        bystate.qa_flowrateaudit(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_flowrateverification(setuppyaqsapi):
    assert (
        bystate.qa_flowrateverification(
            parameter="88101",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2019, month=12, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_one_point_qc(setuppyaqsapi):
    assert (
        bystate.qa_one_point_qc(
            parameter="44201",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="25",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_pep_audit(setuppyaqsapi):
    assert (
        bystate.qa_pep_audit(
            parameter="88101",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_transactionsample(setuppyaqsapi):
    assert (
        bystate.transactionsample(
            parameter="45201",
            bdate=date(year=1995, month=5, day=15),
            edate=date(year=1995, month=5, day=15),
            stateFIPS="37",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_annualperformanceeval(setuppyaqsapi):
    assert (
        bystate.qa_annualperformanceeval(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_annualperformanceevaltransaction(setuppyaqsapi):
    assert (
        bystate.qa_annualperformanceevaltransaction(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_quarterlysummary(setuppyaqsapi):
    assert (
        bystate.quarterlysummary(
            parameter="88101",
            bdate=date(year=2016, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="37",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )
