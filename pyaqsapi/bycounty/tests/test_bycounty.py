from datetime import date
from importlib import import_module
from os import environ
from os.path import abspath, exists
from sys import path

import pytest

# import pyaqsapi.bycounty as bycounty
bycounty = import_module(name="..bycounty", package="pyaqsapi.bycounty")
# from pyaqsapi.helperfunctions import aqs_credentials
helperfunctions = import_module(
    name="..helperfunctions", package="pyaqsapi.helperfunctions"
)


@pytest.fixture
def setuppyaqsapi(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repostiory or in the final package. local loads the AQS user
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


def test_annualsummary_bycounty(setuppyaqsapi):
    assert (
        bycounty.annualsummary(
            parameter="88101",
            bdate=date(year=2016, month=1, day=1),
            edate=date(year=2016, month=2, day=28),
            stateFIPS="37",
            countycode="183",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_dailysummary_bycounty(setuppyaqsapi):
    assert (
        bycounty.dailysummary(
            parameter="88101",
            bdate=date(year=2016, month=1, day=1),
            edate=date(year=2016, month=2, day=28),
            stateFIPS="37",
            countycode="183",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_sampledata_bycounty(setuppyaqsapi):
    assert (
        bycounty.sampledata(
            parameter="88101",
            bdate=date(year=2015, month=1, day=1),
            edate=date(year=2016, month=2, day=28),
            stateFIPS="37",
            countycode="183",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_monitors_bycounty(setuppyaqsapi):
    assert (
        bycounty.monitors(
            parameter="42401",
            bdate=date(year=2015, month=5, day=1),
            edate=date(year=2015, month=5, day=2),
            stateFIPS="15",
            countycode="001",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_collocated_assessments_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_collocated_assessments(
            parameter="88101",
            bdate=date(year=2013, month=1, day=1),
            edate=date(year=2013, month=1, day=31),
            stateFIPS="01",
            countycode="089",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_blanks_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_blanks(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="01",
            countycode="033",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_flowrateaudit_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_flowrateaudit(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="01",
            countycode="033",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_flowrateverification_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_flowrateverification(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="01",
            countycode="033",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_one_point_qc_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_one_point_qc(
            parameter="44201",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="25",
            countycode="001",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_pep_audit_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_pep_audit(
            parameter="88101",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            countycode="089",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_transactionsample_bycounty(setuppyaqsapi):
    assert (
        bycounty.transactionsample(
            parameter="88101",
            bdate=date(year=2016, month=2, day=28),
            edate=date(year=2016, month=2, day=28),
            stateFIPS="37",
            countycode="183",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_annualperformanceeval_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_annualperformanceeval(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            countycode="003",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_qa_annualperformanceevaltransaction_bycounty(setuppyaqsapi):
    assert (
        bycounty.qa_annualperformanceevaltransaction(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            countycode="003",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )


def test_quarterlysummary_bycounty(setuppyaqsapi):
    assert (
        bycounty.quarterlysummary(
            parameter="88101",
            bdate=date(year=2016, month=1, day=1),
            edate=date(year=2017, month=2, day=28),
            stateFIPS="37",
            countycode="183",
            return_header=True,
        )[0].get_status_code()
        == "200"
    )
