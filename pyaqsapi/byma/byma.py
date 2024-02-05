"""Functions that aggregate data by ma (By Monitoring Agency)."""
import pyaqsapi.helperfunctions as helperfunctions


def qa_flowrateaudit(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return Quality assurance flowrate audit data.

    Return a table containing flow rate audit data aggregated by parameter
    code and monitoring agency code (_by_MA) for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame of flow rate audit data
    for FRM PM2.5 January 2016 - January 2018 where the Monitoring Agency is
    the Jefferson County, AL  Department of Health (agency 0550)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_flowrateaudit(parameter="88101",
                                  bdate=date(year=2016, month=1, day=1),
                                  edate=date(year=2018, month=12, day=31),
                                  MA_code="0550")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): flow rate audit data for the
    requested MA_code.
    """
    service = "qaOnePointQcRawData"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_one_point_qc(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table one point QC check data aggregated by monitoring agency
    code (_by_MA).

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame of ozone One Point QC data
    in January 2018 where the Monitoring Agency is the
    Massachusetts Department of Environmental Protection (agency 0660)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_one_point_qc(parameter="44201",
                                 bdate=date(year=2018, month=1, day=1),
                                 edate=date(year=2018, month=1, day=31),
                                 MA_code="0660")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): flow rate audit data for the
    requested MA_code.
    """
    service = "qaFlowRateAudits"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_pep_audit(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of Performance Evaluation Program (PEP) audit data
    aggregated by monitoring agency code (_by_MA) for the time frame between
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
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame of PEP audit data in June 2017 where the
    Monitoring Agency is the Alabama Department
    of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_pep_audit(parameter="88101",
                              bdate=date(year=2017,
                                         month=6,
                                         day=1),
                              edate=date(year=2017,
                                         month=6,
                                         day=30),
                              MA_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance PEP audit data
    for a monitoring agency.
    """
    service = "qaPepAudits"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_blanks(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of blank quality assurance data. Blanks are unexposed
    sample collection devices (e.g., filters) that are transported with the
    exposed sample devices to assess if contamination is occurring during the
    transport or handling of the samples. Data is aggregated by monitoring
    agency code (MA_code).

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame containing PM2.5 blank data in
    January 2018 where the Monitoring Agency is the Alabama
    Department of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_blanks(parameter="88101",
                           bdate=date(year=2018, month=1, day=1),
                           edate=date(year=2018, month=1, day=31),
                           MA_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object):  quality assurance blank sample
    data for all monitors within the input MA_code.
    """
    service = "qaBlanks"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_collocated_assessments(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table of collocated assessment data aggregated by matching input
    parameter, and monitoring agency (MA) code provided for bdate - edate
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
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame containing collocated assessment
    data for FRM PM2.5 January 2013 where the Monitoring Agency is
    the Alabama Department of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_collocated_assessments(parameter="88101",
                                           bdate=date(year=2013,
                                                      month=1,
                                                      day=1),
                                           edate=date(year=2013,
                                                      month=1,
                                                      day=31),
                                           MA_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance collocated
    assessment data for monitors within a monitoring agency.
    """
    service = "qaCollocatedAssessments"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_flowrateverification(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return a table containing flow rate Verification data for a parameter code
    aggregated by matching input parameter, and monitoring agency (MA) code
    provided for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame containing collocated assessment
    data for FRM PM2.5 January 2013 where the Monitoring Agency is
    the Alabama Department of Environmental Management (agency 0013)::

        import pyaqsapi as aqs
        from datetime import date
        ...
        qqs.byma.qa_flowrateverification(parameter="88101",
                                         bdate=date(year=2013,
                                                    month=1,
                                                    day=1),
                                         edate=date(year=2013,
                                                    month=1,
                                                    day=31),
                                         MA_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): flow rate audit data for the
    requested MA_code.
    """
    service = "qaFlowRateVerifications"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def transactionsample(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Return transactionsample data - aggregated by Monitoring agency (MA) in
    the AQS Submission Transaction Format (RD) sample (raw) data for a
    parameter code aggregated by matching input parameter, and monitoring
    agency (MA) code provided for bdate - edate time frame. Includes data both
    in submitted and standard units.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame of ozone transaction sample data for all monitors
    operated by South Coast Air Quality Management District collected
    on May 15, 2015::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.transactionsample(parameter="44201",
                                   bdate=date(year=2015, month=5, day=15),
                                   edate=date(year=2015, month=5, day=15),
                                   MA_code="0972")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): transaction sample (raw) data in
    the AQS submission transaction format (RD) corresponding to the inputs
    provided.
    """
    service = "transactionsSample"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_annualpeferomanceeval(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Returns quality assurance performance evaluation data - aggregated by
    by Monitoring agency (MA) for a parameter code aggregated by matching input
    parameter and MA_code for the time frame between bdate and edate.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame containing annual performance evaluation data for
    ozone where the monitoring agency is the Alabama Department of
    Environmental Management (MA_code 0013).::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_annualpeferomanceeval(parameter="44201",
                                          bdate=date(year=2017,
                                                     month=1,
                                                     day=1),
                                          edate=date(year=2017,
                                                     month=12,
                                                     day=31),
                                          MA_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance performance
    evaluation data. for all monitoring sites for with the MA_code requested
    for the time frame between bdate and edate.
    """
    service = "qaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)


def qa_annualperformanceevaltransaction(
    parameter, bdate, edate, MA_code, cbdate=None, cedate=None, return_header=False
):
    """
    Returns AQS submissions transaction format (RD) of the annual performance
    evaluation data (raw). Includes data pairs for QA - aggregated by
    Monitoring agency (MA) for a parameter code aggregated by matching input
    parameter and MA_code provided for bdate - edate time frame.

    Parameters
    ----------
    parameter : a character list or a single character string
                which represents the parameter code of the air
                pollutant related to the data being requested.
    bdate : a python date object which represents that begin date of the data
            selection. Only data on or after this date will be returned.
    edate : a python date object which represents that end date of the data
            selection. Only data on or before this date will be returned.
    MA_code : a python character object which represents the 4 digit AQS
              Monitoring Agency code (with leading zeroes).
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
    Return a DataFrame containing annual performance evaluation data for
    ozone in where the MA is the Alabama Department of Environmental
    Management (MA_code 0013) for 2017 in RD format.::

        import pyaqsapi as aqs
        from datetime import date
        ...
        aqs.byma.qa_annualperformanceevaltransactionA(parameter="44201",
                                                      bdate=date(year=2017,
                                                                 month=1,
                                                                 day=1),
                                                      edate=date(year=2017,
                                                                 month=12,
                                                                 day=31),
                                                      MA_code="0013")

    Returns
    -------
    (pandas DataFrame or an AQSAPI_V2 object): quality assurance performance
    evaluation data in the AQS submissions transaction format (RD)for all sites
    matching the MA_code requested for the time frame between bdate and edate.
    """
    service = "transactionsQaAnnualPerformanceEvaluations"
    fun = "_aqs_services_by_MA"

    aqsresultlist = helperfunctions._aqsmultiyearcall(
        fun=fun,
        parameter=parameter,
        bdate=bdate,
        edate=edate,
        name1=None,
        name2=None,
        MA_code=MA_code,
        service=service,
        cbdate=cbdate,
        cedate=cedate,
    )

    if return_header:
        return aqsresultlist
    else:
        return helperfunctions.aqs_removeheader(aqsresultlist)
