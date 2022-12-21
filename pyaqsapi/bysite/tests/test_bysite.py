# -*- coding: utf-8 -*-

import pytest
from datetime import date
import pyaqsapi.bysite as bysite
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


def test_sampledata(setuppyaqsapi):
    assert (
        bysite.sampledata(
            parameter="44201",
            bdate=date(year=2017, month=6, day=18),
            edate=date(year=2017, month=6, day=18),
            stateFIPS="37",
            countycode="183",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_annualsummary(setuppyaqsapi):
    assert (
        bysite.annualsummary(
            parameter="44201",
            bdate=date(year=2017, month=6, day=18),
            edate=date(year=2017, month=6, day=18),
            stateFIPS="37",
            countycode="183",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_dailysummary(setuppyaqsapi):
    assert (
        bysite.dailysummary(
            parameter="44201",
            bdate=date(year=2017, month=6, day=18),
            edate=date(year=2017, month=6, day=18),
            stateFIPS="37",
            countycode="183",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_blanks(setuppyaqsapi):
    assert (
        bysite.qa_blanks(
            parameter="44201",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="01",
            countycode="033",
            sitenum="1002",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_monitors(setuppyaqsapi):
    assert (
        bysite.monitors(
            parameter="42401",
            bdate=date(
                year=2015,
                month=5,
                day=1,
            ),
            edate=date(year=2019, month=5, day=2),
            stateFIPS="15",
            countycode="001",
            sitenum="0007",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_collocated_assessments(setuppyaqsapi):
    assert (
        bysite.qa_collocated_assessments(
            parameter="88101",
            bdate=date(
                year=2013,
                month=1,
                day=1,
            ),
            edate=date(
                year=2013,
                month=1,
                day=31,
            ),
            stateFIPS="01",
            countycode="089",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_flowrateaudit(setuppyaqsapi):
    assert (
        bysite.qa_flowrateaudit(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="37",
            countycode="183",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_one_point_qc(setuppyaqsapi):
    assert (
        bysite.qa_one_point_qc(
            parameter="44201",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="25",
            countycode="001",
            sitenum="0002",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_flowrateverification(setuppyaqsapi):
    assert (
        bysite.qa_flowrateverification(
            parameter="88101",
            bdate=date(year=2018, month=1, day=1),
            edate=date(year=2018, month=1, day=31),
            stateFIPS="25",
            countycode="001",
            sitenum="0002",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_transactionsample(setuppyaqsapi):
    assert (
        bysite.transactionsample(
            parameter="44201",
            bdate=date(year=2017, month=6, day=18),
            edate=date(
                year=2017,
                month=6,
                day=18,
            ),
            stateFIPS="37",
            countycode="183",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_annualpeferomanceeval(setuppyaqsapi):
    assert (
        bysite.qa_annualpeferomanceeval(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            countycode="003",
            sitenum="0010",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_quarterlysummary(setuppyaqsapi):
    assert (
        bysite.quarterlysummary(
            parameter="88101",
            bdate=date(year=2016, month=1, day=1),
            edate=date(year=2016, month=1, day=31),
            stateFIPS="37",
            countycode="183",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_pep_audit(setuppyaqsapi):
    assert (
        bysite.qa_pep_audit(
            parameter="88101",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2019, month=12, day=31),
            stateFIPS="01",
            countycode="089",
            sitenum="0014",
            return_header=True,
        )[0].get_status_code()
        == 200
    )


def test_qa_annualperformanceevaltransaction(setuppyaqsapi):
    assert (
        bysite.qa_annualperformanceevaltransaction(
            parameter="44201",
            bdate=date(year=2017, month=1, day=1),
            edate=date(year=2017, month=12, day=31),
            stateFIPS="01",
            countycode="003",
            sitenum="0010",
            return_header=True,
        )[0].get_status_code()
        == 200
    )
