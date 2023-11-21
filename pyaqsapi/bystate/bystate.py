# -*- coding: utf-8 -*-
"""Functions that aggregated data by state."""

from pandas import DataFrame

import pyaqsapi.helperfunctions as helperfunctions


def monitors(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a table of monitors.

    Return a table of monitors and related metadata at all sites
    with the provided parameter and stateFIPS for bdate - edate time frame.

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
    Return a DataFrame of SO2 monitors in Hawaii that were operating on
    May 01, 2017.

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.monitors(parameter="88101",
                             bdate=date(year=2017, month=1, day=1),
                             edate=date(year=2017, month=12, day=31),
                             stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): monitors from the
            selected state.
    """
    service = "monitors"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_flowrateaudit(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return Quality assurance flowrate audit data.

    Return a table of monitors and related metadata at all sites
    with the provided parameter and stateFIPS for bdate - edate time frame.

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
    Return a DataFrame of flow rate audit
    data for Alabama in January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_flowrateaudit(parameter="88101",
                                     bdate=date(year=2018,
                                                month=1,
                                                day=1),
                                     edate=date(year=2018,
                                                month=1,
                                                day=31),
                                     stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): monitors from the
            selected state.
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_one_point_qc(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a DataFrame or an AQS_Data Mart_APIv2 S3 object containing Quality
    assurance data - flow rate audit raw data aggregated by state FIPS for
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
    Return a DataFrame of one point QC check
    data for ozone in Massachusetts in January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_one_point_qc(parameter="44201",
                                    bdate=date(year=2018, month=1, day=1),
                                    edate=date(year=2018, month=1, day=31),
                                    stateFIPS="25")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): one point qc data within the
    input stateFIPS for bdate - edate time frame..
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_pep_audit(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a table of Performance Evaluation Program (PEP) audit data
    aggregated by parameter code, and stateFIPS for the time frame between
    bdate and edate.

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
    Return a DataFrame of PEP audit data for PM2.5 in Alabama 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_pep_audit(parameter="88101",
                                 bdate=date(year=2017, month=1, day=1),
                                 edate=date(year=2017, month=12, day=31),
                                 stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance PEP audit data
    within a state.
    """
    service = "qaPepAudits"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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
    stateFIPS,
    cbdate=None,
    cedate=None,
    duration=None,
    return_header=False,
):
    """
    Return sample data where the data is aggregated at the state level.

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

    Example
    -------
    Return a DataFrame with all benzene samples from
    North Carolina collected from May 15th, 1995 - May 15, 1999::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.sampledata(parameter="45201",
                               bdate=date(year=1995, month=5, day=15),
                               edate=date(year=1995, month=5, day=15),
                               stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): containing sample data
    for all monitors matching stateFIPS for the given parameter.
    """
    service = "sampleData"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
        name1=None,
        name2=None,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
        duration=duration,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def annualsummary(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a DataFrame of annual data aggregated at the state level.

    Annual summary contains a DataFrame matching the input parameter and
    stateFIPS provided for bdate - edate time frame. Variables returned include
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
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
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
    Return a DataFrame with all benzene samples from
    North Carolina collected from May 15th, 1995 - May 15, 1999::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.annualsummary(parameter="45201",
                                  bdate=date(year=1995, month=5, day=15),
                                  edate=date(year=1999, month=5, day=15),
                                  stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): annual summary data for the
    stateFIPS requested.
    """
    service = "annualData"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_blanks(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a table of blank quality assurance data. Blanks are unexposed
    sample collection devices (e.g., filters) that are transported with the
    exposed sample devices to assess if contamination is occurring during
    the transport or handling of the samples. Data is aggregated at the state
    level.

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
    Return a DataFrame which contains PM2.5 blank data
    for Alabama for January 2018::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_blanks(parameter="45201",
                              bdate=date(year=1995, month=5, day=15),
                              edate=date(year=1999, month=5, day=15),
                              stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object):  quality assurance blank sample
    data for all monitors within the input stateFIPS.

    """
    service = "qaBlanks"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a DataFrame of data aggregated at the state level.

    Daily summary contains a DataFrame matching the input parameter and
    stateFIPS provided for bdate - edate time frame. Variables
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
    Return a DataFrame of all benzene daily
    summaries from North Carolina collected on May 15th, 1995::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.dailysummary(parameter="45201",
                                 bdate=date(year=1995, month=5, day=15),
                                 edate=date(year=1995, month=5, day=15),
                                 stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): daily summary statistics for the
    given parameter for a single stateFIPS.
    """
    service = "dailyData"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_collocated_assessments(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a table of collocated assessment data aggregated by matching input
    parameter and stateFIPS provided for bdate - edate time frame.

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
    Return a DataFrame of collocated
    assessment data for FRM2.5 for January 2013::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_collocated_assessments(parameter="88101",
                                              bdate=date(year=2013,
                                                         month=1,
                                                         day=1),
                                              edate=date(year=2013,
                                                         month=1,
                                                         day=31),
                                              stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance collocated
    assessment data for monitors within a state.
    """
    service = "qaCollocatedAssessments"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_flowrateverification(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a table containing flow rate Verification data for a parameter code
    aggregated matching input parameter, and stateFIPS, provided for
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
    Return a DataFrame of flow rate verification data for the state of
    Alabama for 2017-2019::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_flowrateverification(parameter="88101",
                                            bdate=date(year=2017,
                                                       month=1,
                                                       day=1),
                                            edate=date(year=2019,
                                                       month=12,
                                                       day=31),
                                            stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance flow rate
    verification data for monitors within a state.
    """
    service = "qaFlowRateVerifications"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def transactionsample(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return transactionsample data - aggregated by state in the AQS Submission
    Transaction Format (RD) sample (raw) data for a parameter code aggregated
    by matching input parameter, and stateFIPS provided for bdate - edate time
    frame. Includes data both in submitted and standard units.

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
    Return a DataFrame containing benzene transaction sample data for
    North Carolina on May 15, 1995::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.transactionsample(parameter="45201",
                                      bdate=date(year=1995,
                                                 month=5,
                                                 day=15),
                                      edate=date(year=1995,
                                                 month=5,
                                                 day=15),
                                      stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): transaction sample (raw) data
    in the AQS submission transaction format (RD) corresponding to the inputs
    provided.
    """
    service = "transactionsSample"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_annualperformanceeval(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return quality assurance performance evaluation data - aggregated by
    site for a parameter code aggregated by matching input
    parameter, and stateFIPS provided for bdate - edate time frame.

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
    Return a DataFrame containing annual performance evaluation
    data for ozone in Alabama for 2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_annualperformanceeval(parameter="44201",
                                             bdate=date(year=2017,
                                                        month=1,
                                                        day=1),
                                             edate=date(year=2017,
                                                        month=12,
                                                        day=31),
                                             stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    performance evaluation data for all monitoring sites for the
    matching parameter and stateFIPS requested for the time frame
    between bdate and edate.
    """
    service = "qaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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


def qa_annualperformanceevaltransaction(
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return AQS submissions transaction format (RD) of the annual
    performance evaluation data (raw). Includes data pairs for
    QA - aggregated by county for a parameter code aggregated by matching
    input parameter and stateFIPS provided for
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
    Return a DataFrame containing annual performance evaluation data
    for ozone in Alabama for 2017 in RD format.::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.qa_annualperformanceevaltransaction(parameter="44201",
                                                        bdate=date(year=2017,
                                                                   month=1,
                                                                   day=1),
                                                        edate=date(year=2017,
                                                                   month=12,
                                                                   day=31),
                                                        stateFIPS="01")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    performance evaluation data. for all monitoring sites with matching
    parameter and stateFIPS requested for the time frame
    between bdate and edate.
    """
    service = "transactionsQaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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
    parameter,
    bdate,
    edate,
    stateFIPS,
    cbdate=None,
    cedate=None,
    return_header=False,
):
    """
    Return a DataFrame of quarterly data aggregated at the state level.

    Quarterly summary contains a DataFrame matching the input parameter,
    stateFIPS a provided for bdate - edate time frame. Variables returned
    include mean value, maxima, percentiles, and etc.

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
    stateFIPS : a python character object which represents the 2 digit
                state FIPS code (with leading zero) for the state being
                requested. Use aqs_states() for the list of available
                FIPS codes.
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
    Return an aqs S3 object containing quarterly summaries for
    FRM/FEM PM2.5 data for North Carolina for each quarter of  2016-2017::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bystate.quarterlysummary(parameter="88101",
                                     bdate=date(year=2016,
                                                month=1,
                                                day=1),
                                     edate=date(year=2017,
                                                month=12,
                                                day=31),
                                     stateFIPS="37")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quarterly summary statistics for
    the given parameter for a all monitors with matching parameter and
    stateFIPS combination within the bdate - edate timeframe.
    """
    service = "quarterlyData"
    fun = "_aqs_services_by_state"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        stateFIPS=stateFIPS,
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
