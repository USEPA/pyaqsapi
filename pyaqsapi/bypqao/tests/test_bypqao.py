
from datetime import date
from os import environ, getcwd
from os.path import abspath, exists
from sys import path

import pytest

import pyaqsapi.bypqao as bypqao
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


def test_qa_blanks_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_blanks(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            pqao_code="0013",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_collocated_assessments_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_collocated_assessments(
            parameter="88101",
            bdate=date(year=2013, month=1, day=1),
            edate=date(year=2013, month=1, day=31),
            pqao_code="0013",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_flowrateaudit_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_flowrateaudit(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            pqao_code="0550",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_flowrateverification_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_flowrateverification(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            pqao_code="0013",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_one_point_qc_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_one_point_qc(
            parameter="44201",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            pqao_code="0550",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_pep_audit_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_pep_audit(
            parameter="88101",
            bdate=date(year=2017, month=6, day=1),
            edate=date(year=2017, month=6, day=30),
            pqao_code="0013",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_annualperformanceeval_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_annualperformanceeval(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            pqao_code="0013",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_annualperformanceevaltransaction_bypqao(setuppyaqsapi):
    assert (
        bypqao.qa_annualperformanceevaltransaction(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            pqao_code="0013",
            return_header=True,
        )[0].get_status_code()
        == 200
    )
