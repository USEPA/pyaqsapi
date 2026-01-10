"""Functions that aggregate data by county."""

from datetime import date

from pandas import DataFrame

import pyaqsapi.helperfunctions as helperfunctions
from pyaqsapi.helperfunctions import AQSAPI_V2


def monitors(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a table of monitors.

    Return a table of monitors and related metadata at sites with the provided
    parameter, stateFIPS and county_code for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return an DataFrame containing all SO2 monitors in
    Hawaii County, HI that were operating on May 1, 2015::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.monitors(parameter="42401",
                              bdate=date(year=2015,
                                         month=5,
                                         day=1),
                              edate=date(year=2015,
                                         month=5,
                                         day=2),
                              stateFIPS="15",
                              countycode="001")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): monitors from
    the selected stateFIPS and county combination.
    """
    # The monitors service is able to pull multiple years of data
    # without making repeated calls to the API but is done this way to
    # maintain consistency. For the aqs_monitors* function using a single API
    # call will allow the function to finish faster for multiyear calls.
    service = "monitors"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_flowrateaudit(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return Quality assurance flowrate audit data.

    Return a table containing flow rate audit data aggregated by parameter
    code, stateFIPS and countycode for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame of flow rate audit data for
    Jefferson County, AL for January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_flowrateaudit(parameter="88101",
                                      bdate=date(year=2018,
                                                 month=1,
                                                 day=1),
                                      edate=date(year=2018,
                                                 month=1,
                                                 day=31),
                                      stateFIPS="01",
                                      countycode="033")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): flow rate audit data for the
    requested stateFIPS and county combination.
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_one_point_qc(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a table containing flow rate audit data aggregated by parameter
    code, stateFIPS and countycode for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame of flow rate audit data for
    Jefferson County, AL for January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_flowrateaudit(parameter="88101",
                                      bdate=date(year=2018,
                                                 month=1,
                                                 day=1),
                                      edate=date(year=2018,
                                                 month=1,
                                                 day=31),
                                      stateFIPS="01",
                                      countycode="033")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): flow rate audit data for the
    requested stateFIPS and county combination.
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_pep_audit(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a table containing quality assurance Performance Evaluation Program
    (PEP) audit data aggregated by parameter code, stateFIPS and countycode for
    bdate - edate time frame.

    Notes
    -----
    The AQS API only allows for a single year of pep audit data
    to be retrieved at a time. This function conveniently extracts date
    information from the bdate and edate parameters then makes repeated
    calls to the AQSAPI retrieving a maximum of one calendar year of data
    at a time. Each calendar year of data requires a separate API call so
    multiple years of data will require multiple API calls. As the number
    of years of data being requested increases so does the length of time
    that it will take to retrieve results. There is also a 5 second wait
    time inserted between successive API calls to prevent overloading the
    API server. This operation has a linear run time of
    /(Big O notation: O/(n + 5 seconds/)/).

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame with PEP Audit data for FRM
    PM2.5 in Madison County, AL for 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_pep_audit(parameter="88101",
                                  bdate=date(year=2017,
                                             month=1,
                                             day=1),
                                  edate=date(year=2017,
                                             month=12,
                                             day=31),
                                  stateFIPS="01",
                                  countycode="089")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance Performance
    Evaluation Program (PEP) audit data for the requested stateFIPS and county
    combination.
    """
    service = "qaPepAudits"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def sampledata(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    duration: str | None = None,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return sample data where the data is aggregated at the county level.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
    duration : an optional python character string that represents the
               parameter duration code that limits returned data to a specific
               sample duration. The default value of None results in
               no filtering based on duration code.Valid durations include
               actual sample durations and not calculated durations such as 8
               hour carbon monoxide or ozone rolling averages, 3/6 day PM
               averages or lead 3 month rolling averages. Use
               aqs_sampledurations() for a list of all available
               duration codes.
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
               parameter duration code that limits returned data to a
               specific sample duration. The default value of None results
               in no filtering based on duration code.Valid durations
               include actual sample durations and not calculated durations
               such as 8 hour carbon monoxide or ozone rolling averages,
               3/6 day PM averages or lead 3 month rolling averages. Use
               aqs_sampledurations() for a list of all available
               duration codes.
    return_header : If FALSE (default) only returns data requested. If TRUE
                    returns a AQSAPI_v2 object.

    Examples
    --------
    Return all FRM/FEM PM2.5 data for Wake County, NC between
    January 1, 2015 - February 28, 2016::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.sampledata(parameter="88101",
                                bdate=date(year=2015, month=1, day=1),
                                edate=date(year=2016, month=2, day=28),
                                stateFIPS="37",
                                countycode="183")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance Performance
    Evaluation Program (PEP) audit data for the requested stateFIPS and county
    combination.
    """
    service = "sampleData"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
        duration=duration,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def annualsummary(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a DataFrame of annual data aggregated at the county level.

    Annual summary contains a DataFrame matching the input parameter,
    stateFIPS and county_code provided for bdate - edate time frame.
    Variables returned include mean value, maxima, percentiles, and etc.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Returns all FRM/FEM PM2.5 data for Wake County, NC between
    January 1, 2015 - February 28, 2016::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.annualsummary(parameter="88101",
                                   bdate=date(year=2016,
                                              month=1,
                                              day=1),
                                   edate=date(year=2016,
                                              month=2,
                                              day=28),
                                   stateFIPS="37",
                                   countycode="183",
                                   return_header=True)

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): annual summary data for the
    requested stateFIPS and county combination.
    """
    service = "annualData"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_blanks(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a table of blank quality assurance data.
    Blanks are unexposed sample collection devices (e.g.,
    filters) that are transported with the exposed sample devices
    to assess if contamination is occurring during the transport
    or handling of the samples. Data is aggregated at the county level.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame with PM2.5 blank data for
    Colbert County, AL for January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_blanks(parameter="88101",
                               bdate=date(year=2018,
                                          month=1,
                                          day=1),
                               edate=date(year=2018,
                                          month=1,
                                          day=31),
                               stateFIPS="01",
                               countycode="033")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): blank quality assurance data for
    the requested stateFIPS and county combination.
    """
    service = "qaBlanks"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def dailysummary(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a DataFrame of data aggregated at the county level.

    Daily summary contains a DataFrame matching the input parameter, stateFIPS
    and county_code provided for bdate - edate time frame. Variables
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
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return an aqs S3 object of daily summary FRM/FEM PM2.5 data
    for Wake County, NC between January and February 2016::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.dailysummary(parameter="88101",
                                  bdate=date(year=2016,
                                             month=1,
                                             day=1),
                                  edate=date(year=2016,
                                             month=2,
                                             day=28),
                                  stateFIPS="37",
                                  countycode="183")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): blank quality assurance data for
    the requested stateFIPS and county combination.
    """
    service = "dailyData"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_collocated_assessments(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a table of collocated assessment data aggregated by matching input
    parameter, stateFIPS and county_code provided for bdate - edate time
    frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame with collocated assessment data
    for FRM PM2.5 in Madison County, AL for January 2013::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_collocated_assessments(parameter="88101",
                                               bdate=date(year=2013,
                                                          month=1,
                                                          day=1),
                                               edate=date(year=2013,
                                                          month=1,
                                                          day=31),
                                               stateFIPS="01",
                                               countycode="089")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    collocated assessment data for monitors within a county.
    """
    service = "qaCollocatedAssessments"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_flowrateverification(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a table containing flow rate Verification data for a parameter code
    aggregated matching input parameter, stateFIPS, and county_code, provided
    for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Returns a DataFrame of flow rate verification data for
    Colbert County, AL for January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_flowrateverification(parameter="88101",
                                             bdate=date(year=2018,
                                                        month=1,
                                                        day=1),
                                             edate=date(year=2018,
                                                        month=1,
                                                        day=31),
                                             stateFIPS="01",
                                             countycode="033")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance flow rate
    verification data for monitors within a county.
    """
    service = "qaFlowRateVerifications"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def transactionsample(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return transactionsample data - aggregated by county in the AQS Submission
    Transaction Format (RD) sample (raw) data for a parameter code aggregated
    by matching input parameter, stateFIPS and countycode provided for
    bdate - edate time frame. Includes data both in submitted and
    standard units.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return all FRM/FEM transaction data for
    Wake County, NC on February 23, 2016::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.transactionsample(parameter="88101",
                                       bdate=date(year=2016,
                                                  month=2,
                                                  day=28),
                                       edate=date(year=2016,
                                                  month=2,
                                                  day=28),
                                       stateFIPS="37",
                                       countycode="183")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): transaction sample (raw) data
    in the AQS submission transaction format (RD) corresponding to the inputs
    provided.
    """
    service = "transactionsSample"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_annualperformanceeval(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return quality assurance performance evaluation data - aggregated by
    site for a parameter code aggregated by matching input
    parameter, stateFIPS and countycode provided for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame containing annual performance evaluation data (raw)
    for ozone in Baldwin County, AL for 2017 in RD format::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.annualperformanceeval(parameter="44201",
                                           bdate=date(year=2017,
                                                      month=1,
                                                      day=1),
                                           edate=date(year=2017,
                                                      month=12,
                                                      day=31),
                                           stateFIPS="01",
                                           countycode="003")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    performance evaluation data for all monitoring sites for the
    matching countycode and stateFIPS requested for the time frame
    between bdate and edate.
    """
    service = "qaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_annualperformanceevaltransaction(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return AQS submissions transaction format (RD) of the annual
    performance evaluation data (raw). Includes data pairs for
    QA - aggregated by county for a parameter code aggregated by matching
    input parameter, countycode and stateFIPS provided for
    bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame containing annual performance evaluation data (raw)
    for ozone in Baldwin County, AL for 2017 in RD format::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.qa_annualperformanceevaltransaction(parameter="44201",
                                                         bdate=date(year=2017,
                                                                    month=1,
                                                                    day=1),
                                                         edate=date(year=2017,
                                                                    month=12,
                                                                    day=31),
                                                         stateFIPS="01",
                                                         countycode="003")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    performance evaluation data. for all monitoring sites with matching
    countycode and stateFIPS requested for the time frame
    between bdate and edate.
    """
    service = "transactionsQaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def quarterlysummary(
    parameter: str,
    bdate: date,
    edate: date,
    stateFIPS: str,
    countycode: str,
    cbdate: date | None = None,
    cedate: date | None = None,
    return_header: bool | None = False,
) -> DataFrame | AQSAPI_V2 | list[DataFrame] | None | list[AQSAPI_V2]:
    """
    Return a DataFrame of quarterly data aggregated at the county level.

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
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
    countycode : a python character object which represents the 3 digit
                 state FIPS code for the county being requested
                 (with leading zero(s)). Use aqs_counties_by_state() for
                 the list of available county codes for each state.
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

    Examples
    --------
    Return a DataFrame containing quarterly summaries for
    FRM/FEM PM2.5 data for Wake County, NC for each quarter of 2016::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bycounty.quarterlysummary(parameter="88101",
                                      bdate=date(year=2016,
                                                 month=1,
                                                 day=1),
                                      edate=date(year=2017,
                                                 month=2,
                                                 day=28),
                                      stateFIPS="37",
                                      countycode="183")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quarterly summary statistics for
    the given parameter for a single countycode and stateFIPS combination.
    """
    service = "quarterlyData"
    fun = "_aqs_services_by_county"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        countycode=countycode,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    if not return_header:
        return helperfunctions.aqs_removeheader(aqsresultlist)
