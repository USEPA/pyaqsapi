"""metadatafunctions."""
import pyaqsapi.helperfunctions as helperfunctions


def aqs_is_available(return_header=False):
    """
    Return the status of the AQS API.

    Parameters
    ----------
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Details the status of the
    AQS API (The status information is located in the header).
    """
    service = "metaData"
    filter1 = "isAvailable"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_metadata_services(service=service, filter1=filter1)

    if return_header:
        return aqsresult
    else:
        # for the isAvailable service the information is stored in the data.
        return aqsresult.get_data()


def aqs_knownissues(return_header=False):
    """
    Return a table of any known issues with system functionality or the data.
    These are usually issues that have been identified internally and will
    require some time to correct in Data Mart or the API. This function
    implements a direct API call to Data Mart and returns data directly from
    the API. Issues returned via this function do not include any issues from
    the pyaqsapi python package.

    Parameters
    ----------
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Information involving known
    issues with the Data Mart API.
    """
    service = "metaData"
    filter1 = "issues"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_metadata_services(service=service, filter1=filter1)
    if return_header:
        return aqsresult
    else:
        return aqsresult.get_data()


def aqs_revisionhistory(return_header=False):
    """
    Return the change history to the AQS Data Mart API.

    Parameters
    ----------
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Information on the revision
    history to the AQS Datamart API.
    """
    service = "metaData"
    filter1 = "revisionHistory"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_metadata_services(service=service, filter1=filter1)
    if return_header:
        return aqsresult
    else:
        return aqsresult.get_data()
