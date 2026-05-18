"""retrieve ambient air monitoring data from the United States
Environmental Protection Agency’s (US EPA)
Air Quality System (AQS) Data Mart API v2 interface."""

from pyaqsapi import bybox as bybox
from pyaqsapi import bycbsa as bycbsa
from pyaqsapi import bycounty as bycounty
from pyaqsapi import byma as byma
from pyaqsapi import bypqao as bypqao
from pyaqsapi import bysite as bysite
from pyaqsapi import bystate as bystate
from pyaqsapi import helperfunctions as helperfunctions
from pyaqsapi import listfunctions as listfunctions
from pyaqsapi import metadatafunctions as metadatafunctions
from pyaqsapi import setupfunctions as setupfunctions

from .helperfunctions import AQSAPI_V2, AQS_key, AQS_user, _aqsmultiyearcall, aqs_credentials, aqs_removeheader
from .listfunctions import (
    aqs_cbsas,
    aqs_classes,
    aqs_counties_by_state,
    aqs_fields_by_service,
    aqs_mas,
    aqs_parameters_by_class,
    aqs_pqaos,
    aqs_sampledurations,
    aqs_sites_by_county,
    aqs_states,
)
from .metadatafunctions import (  # type: ignore[assignment]
    aqs_is_available,
    aqs_knownissues,
    aqs_revisionhistory,
)
from .setupfunctions import aqs_sign_up

__all__ = [
    "helperfunctions",
    "metadatafunctions",
    "setupfunctions",
    "bysite",
    "bycounty",
    "bystate",
    "byma",
    "bypqao",
    "bycbsa",
    "bybox",
    "listfunctions",
]
