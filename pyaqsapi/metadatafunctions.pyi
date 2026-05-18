from pandas import DataFrame

from pyaqsapi import helperfunctions as helperfunctions
from pyaqsapi.helperfunctions import AQSAPI_V2 as AQSAPI_V2

def aqs_is_available(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return the status of the AQS API.

    Parameters
    ----------
    return_header : If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Details the status of the
    AQS API (The status information is located in the header).
    """

def aqs_knownissues(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of any known issues with system functionality or the data.
    These are usually issues that have been identified internally and will
    require some time to correct in Data Mart or the API. This function
    implements a direct API call to Data Mart and returns data directly from
    the API. Issues returned via this function do not include any issues from
    the pyaqsapi python package.

    Parameters
    ----------
    return_header : If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Information involving known
    issues with the Data Mart API.
    """

def aqs_revisionhistory(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return the change history to the AQS Data Mart API.

    Parameters
    ----------
    return_header : If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Information on the revision
    history to the AQS Datamart API.
    """
