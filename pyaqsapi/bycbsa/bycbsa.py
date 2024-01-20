"""Functions that aggregate data by cbsa
(by Core Based Statistic Area, as defined by the Census Bureau)."""

from pandas import DataFrame

import pyaqsapi.helperfunctions as helperfunctions


def monitors(
    parameter, bdate, edate, cbsa_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of monitors.

    Return a table of monitors at all sites with the provided parameter,
    aggregated by Core Based Statistical Area (CBSA) for bdate - edate
    time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    cbsa_code: a python character object which represents the 5 digit AQS Core
               Based Statistical Area code (the same as the census code, with
               leading zeros)
    cbdate : a python date object which represents a "beginning date of
             last change" that indicates when the data was last updated.
             cbdate is used to filter data based on the change date.
             Only data that changed on or after this date will be returned.
             This is an optional variable which defaults to None.
    cedate : a python date object which represents an "end date of last
             change" that indicates when the data was last updated.
             cedate is used to filter data based on the change date.
             Only data that changed on or before this date will be
             returned. This is an optional variable which defaults
             to None.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Example
    -------
    Return a DataFrame of NO2 monitors for the
    Charlotte-Concord-Gastonia, NC cbsa that were operating
    on January 01, 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycbsa.monitors(parameter="42602",
                            bdate=date(year=2017, month=1, day=1),
                            edate=date(year=2017, month=1, day=1),
                            cbsa_code="16740")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance flow rate
    verification data for monitors at a site.
    """
    # The monitors service does not is able to oull multiple years of data
    # without making repeated calls to the API but is done this way to
    # maintain consistency. For the aqs_monitors* function using a single API
    # call will allow the function to finish faster for multiyear calls.
    service = "monitors"
    fun = "_aqs_services_by_cbsa"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        cbsa_code=cbsa_code,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def sampledata(
    parameter,
    bdate,
    edate,
    cbsa_code,
    duration=None,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return sample data where the data is aggregated at the Core Based
    Statistical Area (cbsa) level.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    cbsa_code: a python character object which represents the 5 digit AQS Core
               Based Statistical Area code (the same as the census code, with
               leading zeros)
    cbdate : a python date object which represents a "beginning date of
             last change" that indicates when the data was last updated.
             cbdate is used to filter data based on the change date.
             Only data that changed on or after this date will be returned.
             This is an optional variable which defaults to None.
    cedate : a python date object which represents an "end date of last
             change" that indicates when the data was last updated.
             cedate is used to filter data based on the change date.
             Only data that changed on or before this date will be
             returned. This is an optional variable which defaults
             to None.
    duration : an optional python character string that represents the
               parameter duration code that limits returned data to a specific
               sample duration. The default value of None results in
               no filtering based on duration code.Valid durations include
               actual sample durations and not calculated durations such as 8
               hour carbon monoxide or ozone rolling averages, 3/6 day PM
               averages or lead 3 month rolling averages. Use
               aqs_sampledurations() for a list of all available
               duration codes.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Example
    -------
    Return a DataFrame which contains NO2 data
    for Charlotte-Concord-Gastonia, NC cbsa for
    January 1, 2015 - January 01, 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycbsa.sampledata(parameter="42602",
                              bdate=date(year=2015, month=1, day=1),
                              edate=date(year=2017, month=1, day=1),
                              cbsa_code="16740")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): sample data for all monitors
    matching cbsa_code for the given parameter.
    """
    service = "sampleData"
    fun = "_aqs_services_by_cbsa"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        cbsa_code=cbsa_code,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def annualsummary(
    parameter, bdate, edate, cbsa_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a DataFrame of annual data aggregated at the Core Based
    Statistical Area (cbsa) level.

    Annual summary contains a DataFrame matching the input parameter and
    cbsa_code provided for bdate - edate time frame. Variables returned include
    mean value, maxima, percentiles, and etc.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    cbsa_code: a python character object which represents the 5 digit AQS Core
               Based Statistical Area code (the same as the census code, with
               leading zeros)
    cbdate : a python date object which represents a "beginning date of
             last change" that indicates when the data was last updated.
             cbdate is used to filter data based on the change date.
             Only data that changed on or after this date will be returned.
             This is an optional variable which defaults to None.
    cedate : a python date object which represents an "end date of last
             change" that indicates when the data was last updated.
             cedate is used to filter data based on the change date.
             Only data that changed on or before this date will be
             returned. This is an optional variable which defaults
             to None.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Example
    -------
    Return a DataFrame of annual summary NO2
    data the for Charlotte-Concord-Gastonia, NC cbsa on
    January 01, 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycbsa.annualsummary(parameter="42602",
                                 bdate=date(year=2017, month=1, day=1),
                                 edate=date(year=2017, month=1, day=1),
                                 cbsa_code="16740")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): a DataFrame or an
    AQS_Data Mart_APIv2 object that containing annual summary data for the
    cbsa_code requested.
    """
    service = "annualData"
    fun = "_aqs_services_by_cbsa"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        cbsa_code=cbsa_code,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def dailysummary(
    parameter, bdate, edate, cbsa_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a DataFrame of data aggregated by Core Based Statistical Area
    (cbsa).

    Daily summary contains a DataFrame matching the input parameter and
    cbsa_code provided for bdate - edate time frame. Variables
    returned include mean value, maxima, percentiles, and etc.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    cbsa_code: a python character object which represents the 5 digit AQS Core
               Based Statistical Area code (the same as the census code, with
               leading zeros)
    cbdate : a python date object which represents a "beginning date of
             last change" that indicates when the data was last updated.
             cbdate is used to filter data based on the change date.
             Only data that changed on or after this date will be returned.
             This is an optional variable which defaults to None.
    cedate : a python date object which represents an "end date of last
             change" that indicates when the data was last updated.
             cedate is used to filter data based on the change date.
             Only data that changed on or before this date will be
             returned. This is an optional variable which defaults
             to None.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Example
    -------
    Returns a DataFrame of NO2 daily summary
    data the for Charlotte-Concord-Gastonia, NC cbsa on
    January 01, 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycbsa.dailysummary(parameter="42602",
                                bdate=date(year=2017, month=1, day=1),
                                edate=date(year=2017, month=1, day=1),
                                cbsa_code="16740")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): a DataFrame or an
    AQS_Data Mart_APIv2 object that containing daily summary data for
    the cbsa_code requested.
    """
    service = "dailyData"
    fun = "_aqs_services_by_cbsa"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        cbsa_code=cbsa_code,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def quarterlysummary(
    parameter, bdate, edate, cbsa_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return quarterly summary data aggregated by Core Based Statistical Area
    (cbsa_code).

    Note
    ----
    The AQS API only allows for a single year of quarterly summary to be
    retrieved at a time. This function conveniently extracts date
    information from the bdate and edate parameters then makes repeated
    calls to the AQSAPI retrieving a maximum of one calendar year of data
    at a time. Each calendar year of data requires a separate API call so
    multiple years of data will require multiple API calls. As the number
    of years of data being requested increases so does the length of time
    that it will take to retrieve results. There is also a 5 second wait
    time inserted between successive API calls to prevent overloading the
    API server. This operation has a linear run time of
    /(Big O notation: O/(n + 5 seconds/)/).

    Also Note that for quarterly data, only the year portion of the bdate
    and edate are used and all 4 quarters in the year are returned.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    cbsa_code: a python character object which represents the 5 digit AQS Core
               Based Statistical Area code (the same as the census code, with
               leading zeros).
    cbdate : a python date object which represents a "beginning date of
             last change" that indicates when the data was last updated.
             cbdate is used to filter data based on the change date.
             Only data that changed on or after this date will be returned.
             This is an optional variable which defaults to None.
    cedate : a python date object which represents an "end date of last
             change" that indicates when the data was last updated.
             cedate is used to filter data based on the change date.
             Only data that changed on or before this date will be
             returned. This is an optional variable which defaults
             to None.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.
    Example
    -------
    Return a DataFrame of NO2 quarterly summary
    data the for Charlotte-Concord-Gastonia, NC cbsa for
    each quarter in 2017.::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycbsa.quarterlysummary(parameter="42602",
                                    bdate=date(year=2017, month=1, day=1),
                                    edate=date(year=2017, month=1, day=1),
                                    cbsa_code="16740")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quarterly summary statistics for
    the given parameter for a all monitors with matching parameter and
    cbsa_code combination within the bdate - edate timeframe.
    """
    service = "quarterlyData"
    fun = "_aqs_services_by_cbsa"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        cbsa_code=cbsa_code,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)
