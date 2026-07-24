from datetime import date
from os import environ
from os.path import abspath, exists
from sys import path

import pytest
from pandas import DataFrame
from pyaqsapi import helperfunctions
from pyaqsapi.helperfunctions import aqs_credentials
from pyaqsapi import metadatafunctions


@pytest.fixture
def setuppyaqsapi(autouse=True):
    if exists("./dev/local.py"):
        # the following should only execute if the file ./dev/local.py exists
        # under the project root folder. This file should not exist on the git
        # repository or in the final package. local loads the AQS user
        # credentials for testing
        path.append(abspath("./dev"))
        import local  # type: ignore[import-not-found]

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


# none of the other test functions use aqsremove_header, so we create a unit
# test to make sure that
def test_aqs_removeheader(setuppyaqsapi):
    returnvalue = metadatafunctions.aqs_knownissues(return_header=False)
    assert isinstance(returnvalue, DataFrame)


# _aqsmultiyearcall used to unpack each call row positionally, so when a caller
# passed cbdate/cedate but not duration the values slid into the wrong
# parameters. This runs offline (no credentials): the service helper is
# monkeypatched, so the request never reaches the network.
def test_multiyearcall_keeps_cbdate_cedate_aligned(monkeypatch):
    captured = {}

    def rec(self, parameter=None, bdate=None, edate=None, stateFIPS=None,
            service=None, duration=None, cbdate=None, cedate=None):
        captured.update(duration=duration, cbdate=cbdate, cedate=cedate)
        return None

    monkeypatch.setattr(helperfunctions.AQSAPI_V2, "_aqs_services_by_state", rec)
    cb, ce = date(2018, 3, 1), date(2018, 4, 1)
    helperfunctions._aqsmultiyearcall(
        fun="_aqs_services_by_state",
        parameter="88101",
        bdate=date(2018, 1, 1),
        edate=date(2018, 12, 31),
        stateFIPS="01",
        service="dailyData",
        cbdate=cb,
        cedate=ce,
    )
    assert captured == {"duration": None, "cbdate": cb, "cedate": ce}
