"""listfunctions."""

from pandas import DataFrame

from pyaqsapi import helperfunctions
from pyaqsapi.helperfunctions import AQSAPI_V2


def aqs_counties_by_state(stateFIPS: str, return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of all counties in within the stateFIPS provided.

    Parameters
    ----------
    stateFIPS : str
                a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    return_header : bool, optional, default=True
                    If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Returns a DataFrame of all the counties
    in North Carolina the county FIPS codes (county codes) for each.::

        aqs_counties_by_state(stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): all counties in the requested
    state.

    """
    aqsfilter = "countiesByState"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter, stateFIPS=stateFIPS)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_sites_by_county(stateFIPS: str, countycode: str, return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of all air monitoring sites with the input state and county FIPS code combination.

    Parameters
    ----------
    stateFIPS : str
                a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : str
                 a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
    return_header : If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of all the counties
    in North Carolina the county FIPS codes (county codes) for each.::

        aqs_counties_by_state(stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): all air monitoring sites with
    the requested state and county FIPS codes.

    """
    aqsfilter = "sitesByCounty"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter, stateFIPS=stateFIPS, countycode=countycode)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_classes(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of Parameter classes or groups of parameters.

    For example, "criteria" "MET" or "all". The information from this function can be used as input to other API calls.


    Parameters
    ----------
    return_header : If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of parameter classes (groups of parameters, i.e.
    "criteria" or all")::

        aqs_classes()

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): Parameter classes (groups of
    parameters, i.e. "criteria" or "all").

    """
    aqsfilter = "classes"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_parameters_by_class(parameterclass: str, return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of parameters in a Parameter class.

    Parameter classes are groups of parameters, i.e. "criteria", "MET" or "all".
    The information from this function can be used as input to other API calls.

    Parameters
    ----------
    parameterclass: str
                    a python character object that represents the class
                    requested, use aqs_classes() for retrieving available
                    classes. The parameterclass python character object must be
                    a valid parameterclass as returned from aqs_classes().
                    The class must be an exact match to what is returned from
                    aqs_classes().
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of parameter classes (groups of parameters, i.e.
    "criteria" or all")::

        aqs_classes()

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): parameters associated with the
    parameterclass requested. None is returned for parameterclasses not found.

    """
    aqsfilter = "parametersByClass"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(parameterclass=parameterclass, aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_mas(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a DataFrame of monitoring agencies (MA).

    Parameters
    ----------
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Returns a DataFrame of monitoring agencies and their respective
    monitoring agency codes.::

        aqs_mas()

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): monitoring agencies and their
    associated agency code.

    """
    aqsfilter = "mas"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_pqaos(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of primary quality assurance organizations (pqaos).

    Parameters
    ----------
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of primary quality assurance organizations (pqaos)::

        aqs_pqaos()

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): pqaos and their associated
    pqao_codes.

    """
    aqsfilter = "pqaos"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_cbsas(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of all Core Based Statistical Areas (cbsa) and their associated cbsa_codes.

    Parameters
    ----------
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of Core Based Statistical Areas (cbsas)
    and their respective cbsa codes::

        aqs_cbsas()

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): all cbsas and their associated
    cbsa_codes.

    """
    aqsfilter = "cbsas"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_states(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of US states, US territories, and the district or Columbia with their respective FIPS codes.

    Parameters
    ----------
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of states and their FIPS codes::

        aqs_states()}

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): states and their associated FIPS
    code.

    """
    aqsfilter = "states"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_fields_by_service(service: str, return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table containing the list and definitions of fields in the service requested.

    Parameters
    ----------
    service : str
              a string which represents the services provided by the AQS
              API. For a list of available services refer to
              https://aqs.epa.gov/aqsweb/documents/data_api.html#services
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame containing a list and definitions
    of fields in the Sample Data service.::

        aqs_fieldsbyservice(service="sampleData")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): details the status of the AQS
        API.

    """
    aqsfilter = "fieldsByService"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_metadata_services(service=service, aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()


def aqs_sampledurations(return_header: bool | None = False) -> AQSAPI_V2 | DataFrame:
    """Return a table of sample durations and their associated duration codes.

    Returned values are not calculated durations such as 8 hour carbon monoxide
    or ozone rolling averages, 3/6 day PM averages or Pb 3 month rolling
    averages.


    Parameters
    ----------
    return_header : bool, optional, default=False
                    If False (default) only returns data requested. If True returns a AQSAPI_v2 object.

    Examples
    --------
    Return a DataFrame of::

        aqs_sampledurations()

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): sample durations and
    their associated duration codes.

    """
    aqsfilter = "duration"
    aqsresult = helperfunctions.AQSAPI_V2()
    aqsresult._aqs_list_services(aqsfilter=aqsfilter)
    if return_header:
        return aqsresult
    if not return_header:
        return aqsresult.get_data()
