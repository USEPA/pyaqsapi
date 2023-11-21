# -*- coding: utf-8 -*-
"""Functions that aggregate data by pqao
(By Primary Quality Assurance Organization)."""

import pyaqsapi.helperfunctions as helperfunctions


def qa_flowrateaudit(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return Quality assurance flowrate audit data.

    Return quality assurance flow rate audit data aggregated by parameter code
    and Primary Quality Assurance Organization (PQAO) code for bdate - edate
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
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    Return a DataFrame of flow rate audit data for January
    2018 where the PQAO is the Jefferson County, AL Department Of
    Health (agency 0550).::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bypqao.qa_flowrateaudit(parameter="88101",
                                    bdate=date(year=2018, month=1, day=1),
                                    edate=date(year=2018, month=1, day=31),
                                    pqao_code="0550")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): flow rate audit data for the
    requested pqao_code.
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_one_point_qc(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return Quality assurance data - collocated assessment raw data aggregated
    by Primary Quality Assurance Organization (PQAO) code.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    Return a DataFramee of flow rate audit data for January 2018 where the
    PQAO is the Jefferson County, AL Department of Health (agency 0550)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bypqao.qa_one_point_qc(parameter="44201",
                                   bdate=date(year=2018,
                                              month=1,
                                              day=1),
                                   edate=date(year=2018,
                                              month=1,
                                              day=31),
                                   pqao_code="0550")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): one point qc data within a pqao
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_pep_audit(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of Performance Evaluation Program (PEP) audit data
    aggregated by Primary Quality Assurance Organization (PQAO) code for the
    time frame between bdate and edate.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    ------
    Return a DataFrame of PEP audit data in June 2017 where the pqao is the
    Alabama Department of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bypqao.qa_pep_audit(parameter="88101",
                                bdate=date(year=2017, month=6, day=1),
                                edate=date(year=2017, month=6, day=30),
                                pqao_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance PEP audit data
    for a Primary Quality Assurance Organization.
    """
    service = "qaPepAudits"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_blanks(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of blank quality assurance data. Blanks are unexposed
    sample collection devices (e.g., filters) that are transported with the
    exposed sample devices to assess if contamination is occurring during the
    transport or handling of the samples. Data is aggregated by Primary Quality
    Assurance Organization (PQAO).

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    Return DataFrame of PM2.5 blank data in January 2018 where the PQAO is
    the Alabama Department of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bypqao.aqs_qa_blanks(parameter="88101",
                                 bdate=date(year=2018, month=1, day=1),
                                 edate=date(year=2018, month=1, day=31),
                                 pqao_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance blank data
    for monitors within a pqao.
    """
    service = "qaBlanks"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_collocated_assessments(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of blank quality assurance data. Blanks are unexposed
    sample collection devices (e.g., filters) that are transported with the
    exposed sample devices to assess if contamination is occurring during the
    transport or handling of the samples. Data is aggregated by Primary Quality
    Assurance Organization (PQAO).

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    Returns a DataFrame of collocated assessment
    data for FRM PM2.5 in January 2013 where the PQAO is the Alabama
    Department of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bypqao.qa_collocated_assessments(parameter="88101",
                                             bdate=date(year=2013,
                                                        moth=1,
                                                        day=1),
                                             edate=date(year=2013,
                                                        month=1,
                                                        day=31),
                                             pqao_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance blank data
    for monitors within a pqao.
    """
    service = "qaCollocatedAssessments"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_flowrateverification(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table containing flow rate Verification data for a parameter code
    aggregated by matching input parameter, and Primary Quality Assurance
    Organization (PQAO) code provided for bdate - edate time.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    Return a DataFrame of collocated assessment
    data for FRM PM2.5 in January 2013 where the PQAO is the Alabama
    Department of Environmental Management (agency 0013)::

        from datetime import date
        import pyaqsapi as aqs
        ...
        aqs.bypqao.aqs_qa_flowrateverification(parameter="88101",
                                               bdate=date(year=2018,
                                                          month=1,
                                                          day=1),
                                               edate=date(year=2018,
                                                          month=1,
                                                          day=31),
                                               pqao_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance flow rate
    verification data for monitors within a pqao.
    """
    service = "qaFlowRateVerifications"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_annualperformanceeval(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return quality assurance performance evaluation data - aggregated by
    Primary Quality Assurance Organization (PQAO) for a parameter
    code aggregated by matching input parameter and pqao_code for the
    time frame between bdate and edate.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    for ozone where the PQAO is the Alabama Department of
    Environmental Management (pqao_code 0013).::

        from datetime import date
        import pyaqsapi as aqs
        ...
        aqs.bypqao.qa_annualperformanceeval(parameter="44201",
                                            bdate=date(year=2017,
                                                       month=1,
                                                       day=1),
                                            edate=date(year=2017,
                                                       month=12,
                                                       day=31),
                                            pqao_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    performance evaluation data. for single monitoring site for the
    pqao_code requested for the time frame between bdate and edate.
    """
    service = "qaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_annualperformanceevaltransaction(
    parameter, bdate, edate, pqao_code, cbdate=None, cedate=None, return_header=False
):
    """
    Returns AQS submissions transaction format (RD) of the annual
    performance evaluation data (raw). Includes data pairs for
    QA - aggregated by Primary Quality Assurance Organization (PQAO)
    for a parameter code aggregated by matching input parameter and
    pqao_code provided for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    pqao_code : a python character object which represents the 4 digit AQS
                Primary Quality Assurance Organization code
                (with leading zeroes).
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
    Return a DataFrame containing annual performance evaluation data for
    ozone in where the PQAO is the Alabama Department of
    Environmental Management (pqao_code 0013) for 2017 in RD format.::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.bypqao.qa_annualperformanceevaltransaction(parameter="44201",
                                                       bdate=date(year=2017,
                                                                  month=1,
                                                                  day=1),
                                                       edate=date(year=2017,
                                                                  month=12,
                                                                  day=31),
                                                       pqao_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance
    performance evaluation data. for single monitoring site for the
    sitenum, countycode and stateFIPS requested for the time frame
    between bdate and edate
    """
    service = "transactionsQaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_pqao"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        pqao_code=pqao_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)
