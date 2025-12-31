"""Functions that aggregate data by latitude/longitude bounding box."""

from datetime import date

from pandas import DataFrame

import pyaqsapi.helperfunctions as helperfunctions
from pyaqsapi.helperfunctions import AQSAPI_V2


def monitors(
    parameter: str,
    bdate: date,
    edate: date,
    minlat: str,
    maxlat: str,
    minlon: str,
    maxlon: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
):
    """
    Return a table of monitors.

    Return a table of monitors and related metadata sites with the provided
    parameter, aggregated by latitude/longitude bounding box (_by_box) for
    bdate - edate time frame.

    Parameters
    ----------
    parameter : a character string which represents the parameter code of the
                air pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    minlat : a python character object which represents the minimum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data north of this latitude will be returned.
    maxlat : a python character object which represents the maximum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data south of this latitude will be returned.
    minlon : a python character object which represents the minimum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data east of this longitude will be returned.
    maxlon : a python character object which represents the maximum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data west of this longitude will be returned. Note that -80
             is less than -70.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_V2 object.

    Examples
    --------
    Return a DataFrame of all ozone monitors in the vicinity of
    central Alabama that operated in 1995.

    import pyaqsapi as aqs
    from datetime import date

    aqs.bybox.monitors(parameter="44201",
                       bdate=date(year=1995, month=1, day=1),
                       edate=date(year=1995, month=12, day=31),
                       minlat="33.3",
                       maxlat="33.6",
                       minlon="-87.0",
                       maxlon="-86.7")

    Returns
    -------
    pandas DataFrame or an AQSAPI_V2 object
    Returns a table of monitors from a latitude/longitude bounding
    box (_by_box).

    """
    # The monitors service is able to pull multiple years of data
    # without making repeated calls to the API but is done this way to
    # maintain consistency. For the aqs_monitors* function using a single API
    # call will allow the function to finish faster for multiyear calls.
    service = "monitors"
    fun = "_aqs_services_by_box"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        minlat=minlat,
        maxlat=maxlat,
        minlon=minlon,
        maxlon=maxlon,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    return helperfunctions.aqs_removeheader(aqsresultlist)


def sampledata(
    parameter: str,
    bdate: date,
    edate: date,
    minlat: str,
    maxlat: str,
    minlon: str,
    maxlon: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    duration: str | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2:
    """
    Return sample data where the data is aggregated by latitude/longitude
    bounding box (_by_box).

    If return_header is FALSE (default) this function
    returns a single DataFrame with the requested data. If return_header is
    TRUE returns a list of AQSAPI_V2 objects

    Parameters
    ----------
    parameter : a character string which represents the parameter code of the
                air pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    minlat : a python character object which represents the minimum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data north of this latitude will be returned.
    maxlat : a python character object which represents the maximum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data south of this latitude will be returned.
    minlon : a python character object which represents the minimum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data east of this longitude will be returned.
    maxlon : a python character object which represents the maximum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data west of this longitude will be returned. Note that -80
             is less than -70.
    duration : an optional python character string that represents the
               parameter duration code that limits returned data to a
               specific sample duration. The default value of None results
               in no filtering based on duration code.Valid durations
               include actual sample durations and not calculated durations
               such as 8 hour carbon monoxide or ozone rolling averages,
               3/6 day PM averages or lead 3 month rolling averages. Use
               aqs_sampledurations() for a list of all available
               duration codes.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_V2 object.

    Examples
    --------
    Return a DataFrame containing all ozone samples in the vicinity of
    central Alabama between May 1, 2015 - May 2, 2017.

    import pyaqsapi as aqs
    from datetime import date

    aqs.bybox.sampledata(parameter="44201",
                         bdate=date(year=2015, month=5, day=1),
                         edate=date(year=2015, month=5, day=2),
                         minlat="33.3",
                         maxlat="33.6",
                         minlon="-87.0",
                         maxlon="-86.7")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): sample data for all monitors
    within the input latitude/longitude bounding box for a single parameter.
    """
    service = "sampleData"
    fun = "_aqs_services_by_box"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        minlat=minlat,
        maxlat=maxlat,
        minlon=minlon,
        maxlon=maxlon,
        duration=duration,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    return helperfunctions.aqs_removeheader(aqsresultlist)


def annualsummary(
    parameter: str,
    bdate: str,
    edate: str,
    minlat: str,
    maxlat: str,
    minlon: str,
    maxlon: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2:
    """
    Return a DataFrame of annual data aggregated by latitude/longitude
    bounding box (_by_box).

    Annual summary contains a DataFrame matching the input parameter for the
    rectangular area area bounded by minlat, maxlat, minlon, maxlon provided
    for bdate - edate time frame. Variables returned include mean value, maxima,
    percentiles, and etc.

    Parameters
    ----------
    parameter : a character string which represents the parameter code of the
                air pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    minlat : a python character object which represents the minimum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data north of this latitude will be returned.
    maxlat : a python character object which represents the maximum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data south of this latitude will be returned.
    minlon : a python character object which represents the minimum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data east of this longitude will be returned.
    maxlon : a python character object which represents the maximum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data west of this longitude will be returned. Note that -80
             is less than -70.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_V2 object.

    Examples
    --------
    Return a DataFrame containing ozone annual summaries in the vicinity of
    central Alabama for the first two days of May, 2015.

    import pyaqsapi as aqs
    from datetime import date

    aqs.bybox.annualsummary(parameter="44201",
                            bdate=date(year=2015, month=5, day=1),
                            edate=date(year=2015, month=5, day=2),
                            minlat="33.3",
                            maxlat="33.6",
                            minlon="-87.0",
                            maxlon="-86.7")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object) sample data for all monitors
    within the input latitude/longitude bounding box for a single parameter.
    """
    service = "annualData"
    fun = "_aqs_services_by_box"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        minlat=minlat,
        maxlat=maxlat,
        minlon=minlon,
        maxlon=maxlon,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    return helperfunctions.aqs_removeheader(aqsresultlist)


def dailysummary(
    parameter: str,
    bdate: date,
    edate: date,
    minlat: str,
    maxlat: str,
    minlon: str,
    maxlon: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool = False,
) -> DataFrame | AQSAPI_V2:
    """
    Return a DataFrame of daily summary data aggregated by latitude/longitude
    bounding box (_by_box).

    Daily summary contains a DataFrame matching the input parameter and
    stateFIPS provided for bdate - edate time frame. Variables
    returned include mean value, maxima, percentiles, and etc.

    Parameters
    ----------
    parameter : a character string which represents the parameter code of the
                air pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    minlat : a python character object which represents the minimum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data north of this latitude will be returned.
    maxlat : a python character object which represents the maximum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data south of this latitude will be returned.
    minlon : a python character object which represents the minimum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data east of this longitude will be returned.
    maxlon : a python character object which represents the maximum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data west of this longitude will be returned. Note that -80
             is less than -70.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_V2 object.

    Examples
    --------
    Return a DataFrame of ozone daily summaries in the vicinity of
    central Alabama for the first two days of May 2015::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bybox.dailysummary(parameter="44201",
                               bdate=date(year=2015, month=5, day=1),
                               edate=date(year=2015, month=5, day=2),
                               minlat="33.3",
                               maxlat="33.6",
                               minlon="-87.0",
                               maxlon="-86.7")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): daily summary data for all
    monitors within the input latitude/longitude bounding box for a single
    parameter.
    """
    service = "dailyData"
    fun = "_aqs_services_by_box"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        minlat=minlat,
        maxlat=maxlat,
        minlon=minlon,
        maxlon=maxlon,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    return helperfunctions.aqs_removeheader(aqsresultlist)


def quarterlysummary(
    parameter: str,
    bdate: date,
    edate: date,
    minlat: str,
    maxlat: str,
    minlon: str,
    maxlon: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    duration: str | None = None,
    return_header: bool = False,
) -> DataFrame | AQSAPI_V2:
    """
    Return a DataFrame of quarterly data aggregate by latitude/longitude
    bounding box (_by_box).

    Quarterly summary contains a DataFrame matching the input parameter,
    stateFIPS and county_code provided for bdate - edate time frame.
    Variables returned include mean value, maxima, percentiles, and etc.

    Notes
    -----
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
    parameter : a character string which represents the parameter code of the
                air pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    minlat : a python character object which represents the minimum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data north of this latitude will be returned.
    maxlat : a python character object which represents the maximum latitude
             of a geographic box. Decimal latitude with north begin positive.
             Only data south of this latitude will be returned.
    minlon : a python character object which represents the minimum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data east of this longitude will be returned.
    maxlon : a python character object which represents the maximum longitude
             of a geographic box. Decimal longitude with east begin positive.
             Only data west of this longitude will be returned. Note that -80
             is less than -70.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_V2 object.

    Examples
    --------
    Return a DataFrame containing ozone quarterly summaries
    in the vicinity of central Alabama for each quarter in
    between 2015 - 2017::

        from datetime import date
        import pyaqsapi as aqs
        ...
        aqs.bybox.quarterlysummary(parameter="44201",
                                   bdate=date(year=2015, month=1, day=1),
                                   edate=date(year=2017, month=12, day=31),
                                   minlat="33.3",
                                   maxlat="33.6",
                                   minlon="-87.0",
                                   maxlon="-86.7")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): daily summary data for all
    monitors within the input latitude/longitude bounding box for a single
    parameter.
    """
    service = "quarterlyData"
    fun = "_aqs_services_by_box"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        duration=duration,
        minlat=minlat,
        maxlat=maxlat,
        minlon=minlon,
        maxlon=maxlon,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    return helperfunctions.aqs_removeheader(aqsresultlist)
