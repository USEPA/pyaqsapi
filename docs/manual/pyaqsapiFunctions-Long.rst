.. index:: pyaqsapi Functions Long;
.. sectionauthor:: Clinton Mccrowey \<mccrowey \<DOT\>\ clinton \<AT\>\ epa.gov\>

Functions Exported by pyaqsapi
====================================================
The pyaqsapi package includes the following submodules which are not
loaded by default:
::

* pyaqsapi.bysite
* pyaqsapi.bycounty
* pyaqsapi.bycounty
* pyaqsapi.bycbsa
* pyaqsapi.bybox
* pyaqsapi.byma
* pyaqsapi.ma

With these submodules loaded the entire list of functions exported by the
pyaqsapi package includes:

::

* pyaqsapi.aqs_cbsas,
* pyaqsapi.aqs_classes,
* pyaqsapi.aqs_counties_by_state,
* pyaqsapi.aqs_credentials,
* pyaqsapi.aqs_credentials,
* pyaqsapi.aqs_fields_by_service,
* pyaqsapi.aqs_fields_by_service,
* pyaqsapi.aqs_isavailable,
* pyaqsapi.aqs_isavailable,
* pyaqsapi.aqs_knownissues,
* pyaqsapi.aqs_knownissues,
* pyaqsapi.aqs_mas,
* pyaqsapi.aqs_parameters_by_class,
* pyaqsapi.aqs_pqaos,
* pyaqsapi.aqs_removeheader,
* pyaqsapi.aqs_revisionhistory,
* pyaqsapi.aqs_revisionhistory,
* pyaqsapi.aqs_sampledurations,
* pyaqsapi.aqs_sign_up,
* pyaqsapi.aqs_sign_up,
* pyaqsapi.aqs_sites_by_county,
* pyaqsapi.aqs_states,
* pyaqsapi.bybox.annualsummary,
* pyaqsapi.bybox.dailysummary,
* pyaqsapi.bybox.helperfunctions,
* pyaqsapi.bybox.monitors,
* pyaqsapi.bybox.quarterlysummary,
* pyaqsapi.bybox.sampledata,
* pyaqsapi.bycbsa.annualsummary,
* pyaqsapi.bycbsa.dailysummary,
* pyaqsapi.bycbsa.helperfunctions,
* pyaqsapi.bycbsa.monitors,
* pyaqsapi.bycbsa.quarterlysummary,
* pyaqsapi.bycbsa.sampledata,
* pyaqsapi.bycounty.annualsummary,
* pyaqsapi.bycounty.dailysummary,
* pyaqsapi.bycounty.helperfunctions,
* pyaqsapi.bycounty.monitors,
* pyaqsapi.bycounty.qa_annualperformanceeval,
* pyaqsapi.bycounty.qa_annualperformanceevaltransaction,
* pyaqsapi.bycounty.qa_blanks,
* pyaqsapi.bycounty.qa_collocated_assessments,
* pyaqsapi.bycounty.qa_flowrateaudit,
* pyaqsapi.bycounty.qa_flowrateverification,
* pyaqsapi.bycounty.qa_one_point_qc,
* pyaqsapi.bycounty.qa_pep_audit,
* pyaqsapi.bycounty.quarterlysummary,
* pyaqsapi.bycounty.sampledata,
* pyaqsapi.bycounty.transactionsample,
* pyaqsapi.byma.qa_annualpeferomanceeval,
* pyaqsapi.byma.qa_annualperformanceevaltransaction,
* pyaqsapi.byma.qa_blanks,
* pyaqsapi.byma.qa_collocated_assessments,
* pyaqsapi.byma.qa_flowrateaudit,
* pyaqsapi.byma.qa_flowrateverification,
* pyaqsapi.byma.qa_one_point_qc,
* pyaqsapi.byma.qa_pep_audit,
* pyaqsapi.byma.transactionsample,
* pyaqsapi.bypqao.qa_annualperformanceeval,
* pyaqsapi.bypqao.qa_annualperformanceevaltransaction,
* pyaqsapi.bypqao.qa_blanks,
* pyaqsapi.bypqao.qa_collocated_assessments,
* pyaqsapi.bypqao.qa_flowrateaudit,
* pyaqsapi.bypqao.qa_flowrateverification,
* pyaqsapi.bypqao.qa_one_point_qc,
* pyaqsapi.bypqao.qa_pep_audit,
* pyaqsapi.bysite.annualsummary,
* pyaqsapi.bysite.dailysummary,
* pyaqsapi.bysite.helperfunctions,
* pyaqsapi.bysite.monitors,
* pyaqsapi.bysite.qa_annualpeferomanceeval,
* pyaqsapi.bysite.qa_annualperformanceevaltransaction,
* pyaqsapi.bysite.qa_blanks,
* pyaqsapi.bysite.qa_collocated_assessments,
* pyaqsapi.bysite.qa_flowrateaudit,
* pyaqsapi.bysite.qa_flowrateverification,
* pyaqsapi.bysite.qa_one_point_qc,
* pyaqsapi.bysite.qa_pep_audit,
* pyaqsapi.bysite.quarterlysummary,
* pyaqsapi.bysite.sampledata,
* pyaqsapi.bysite.transactionsample,
* pyaqsapi.bystate.annualsummary,
* pyaqsapi.bystate.dailysummary,
* pyaqsapi.bystate.helperfunctions,
* pyaqsapi.bystate.monitors,
* pyaqsapi.bystate.qa_annualperformanceeval,
* pyaqsapi.bystate.qa_annualperformanceevaltransaction,
* pyaqsapi.bystate.qa_blanks,
* pyaqsapi.bystate.qa_collocated_assessments,
* pyaqsapi.bystate.qa_flowrateaudit,
* pyaqsapi.bystate.qa_flowrateverification,
* pyaqsapi.bystate.qa_one_point_qc,
* pyaqsapi.bystate.qa_pep_audit,
* pyaqsapi.bystate.quarterlysummary,
* pyaqsapi.bystate.sampledata,
* pyaqsapi.bystate.transactionsample


pyaqsapi functions are named according to the service and filter variables that
are available by the AQS Data Mart API. Refer to `Air Quality System (AQS) API
<https://aqs.epa.gov/aqsweb/documents/data_api.html>`_ for full details of the
AQS DataMart API.


Variable descriptions and usage
===============================
These are all the available variables that can be used with various functions
exported from the pyaqsapi library listed alphabetically. Not all of these
variables are used with every function, and not all of these parameters are
required. See the :ref: `pyaqsapi functional families` section to
see which parameters are used with each function.

* AQSobject:
    an object of type AQSAPI_V2 that is returned from pyaqsapi
    aggregate functions wheen return_header is True.

* bdate:
    a date object which represents the begin date of the data selection.
    Only data on or after this date will be returned.

* cbdate (optional):
    a date object which represents the "beginning date of last change" that
    indicates when the data was last updated. cbdate is used to filter data
    based on the change date. Only data that changed on or after this
    date will be returned. This is an optional variable which defaults to None.

* cedate (optional):
    a date object which represents the "end date of last change" that indicates
    when the data was last updated. cedate is used to filter data based on the
    change date. Only data that changed on or before this date will be
    returned. This is an optional variable which defaults to None.

* countycode:
    a character object which represents the 3 digit state FIPS code for the
    county being requested (with leading zero(s)). Refer to
    `aqs_counties_by_state()`_ for a table of available county codes for each
    state.

* duration (optional):
    a character string that represents the parameter duration code that limits
    returned data to a specific sample duration. The default value of None
    will result in no filtering based on duration code. Valid durations
    include actual sample durations and not calculated durations such as 8 hour
    CO or O\ :sub:`3`\ rolling averages, 3/6 day PM  averages or Pb 3 month
    rolling averages. Refer to `aqs_sampledurations()`_ for a table of all
    available duration codes.

* edate:
    a date object which represents the end date of the data selection. Only
    data on or before this date will be returned.

* email:
    a character object which represents the email account that will be used to
    register with the AQS API or change an existing user's key. A verification
    email will be sent to the account specified.

* key:
    a character object which represents the key used in conjunction with the
    username given to connect to AQS Data Mart.

* MA_code:
    a character object which represents the 4 digit AQS Monitoring Agency code
    (with leading zeroes).

* maxlat:
    a character object which represents the maximum latitude of a geographic
    box. Decimal latitude with north begin positive. Only data south of this
    latitude will be returned.

* maxlon:
    a character object which represents the maximum longitude of a
    geographic box. Decimal longitude with east being positive. Only
    data west of this longitude will be returned. Note that -80 is less
    than -70.

* minlat:
    a character object which represents the minimum latitude of a
    geographic box. Decimal latitude with north being positive.
    Only data north of this latitude will be returned.

* minlon:
    a character object which represents the minimum longitude of a
    geographic box. Decimal longitude with east begin positive. Only
    data east of this longitude will be returned.

* parameter:
    a character list or single character object which represents the parameter
    code of the air pollutant related to the data being requested.

* return_Header:
    If False (default) only returns data requested as a pandas DataFrame. If
    True returns a AQSAPI_V2 object.

* service:
    a string which represents the services provided by the AQS API. For a list
    of available services refer to
    `<https://aqs.epa.gov/aqsweb/documents/data_api.html#services>_`
    for the complete listing of services available through the EPA
    AQS Datamart API

* sitenum:
    a character object which represents the 4 digit site number (with
    leading zeros) within the county and state being requested.

* stateFIPS:
    a character object which represents the 2 digit state FIPS code
    (with leading zero) for the state being requested.

* pqao_code:
    a character object which represents the 4 digit AQS Primary Quality
    Assurance Organization code (with leading zeroes).

* username:
    a character object which represents the email account that will be used to
    connect to the AQS API.

pyaqsapi functional families
============================

Sign up and credentials
-----------------------
The functions included in this family of functions are:

::

* aqs_credentials
* aqs_sign_up

These functions are used to sign up with Data Mart and to store credential
    information to use with pyaqsapi. The aqs_sign_up function takes
    one parameter:

* email:

The aqs_credentials function takes two parameters:

* username:
* key:

Data Mart API metadata functions
--------------------------------
The functions included in this family of functions are:

::

* aqs_isavailable
* aqs_knownissues
* aqs_fields_by_service
* aqs_revisionhistory

These functions return Data Mart meta data

    The aqs_isavailable function takes no parameters and returns a
    table which details the status of the AQS API.

    The aqs_fields_by_service function takes one parameter, service,
    which is a character object which represents the services provided by
    the AQS API. For a list of available services see
    `Air Quality System (AQS) API - Services Overview
    <https://aqs.epa.gov/aqsweb/documents/data_api.html#services>`_

    The aqs_knownissues function takes no parameters and Returns a
    table of any known issues with system functionality or the data. These are
    usually issues that have been identified internally and will require some
    time to correct in Data Mart or the API. This function implements a direct
    API call to Data Mart and returns data directly from the API. Issues
    returned via this function do not include any issues from the pyaqsapi
    package.

    The aqs_revisionhistory function is used to query Data Mart for the
    change history to the API.

Data Mart API list functions
----------------------------
The functions included in this family of functions are:
::

* aqs_cbsas,
* aqs_classes,
* aqs_counties_by_state,
* aqs_fields_by_service,
* aqs_isavailable,
* aqs_knownissues,
* aqs_mas,
* aqs_parameters_by_class,
* aqs_pqaos,
* aqs_revisionhistory,
* aqs_sampledurations,
* aqs_sites_by_county,
* aqs_states


    List functions return the API status, API options or groupings that can be
    used in conjunction with other API calls. By default each function in this
    category returns results as a DataTable. If return_header parameter is set
    to True a AQSAPI_v2 object is returned instead.

    aqs_cbsas returns a table of all available Core Based Statistical
    Areas (cbsas) and their respective cbsa codes.

    aqs_states takes no arguments and returns a table of the available
    states and their respective state FIPS codes.

    _`aqs_sampledurations()`
    aqs_sampledurations takes no arguments and returns a table of the
    available sample duration code used to construct other requests.

    aqs_classes takes no arguments and returns a table of parameter
    classes (groups of parameters, i.e. "criteria" or "all").

    _`aqs_counties_by_state()`
    aqs_counties_by_state takes one parameter, stateFIPS, which is a two
    digit state FIPS code for the state being requested represented as a
    character object and returns a table of counties and their
    respective FIPS code for the state requested. Use aqs_states to
    receive a table of valid state FIPS codes.

    aqs_sites_by_county takes two parameters, stateFIPS, which is a
    two digit state FIPS code for the state being requested and county_code
    which is a three digit county FIPS code for the county being requested,
    both stateFIPS and county_code should be encoded as a character object.
    This function returns a table of all air monitoring sites with the
    requested state and county FIPS code combination.

    aqs_pqaos takes no parameters and returns an AQSAPI_V2
    object containing a table of primary quality assurance
    organizations (pqaos).

    aqs_mas takes no parameters and returns an AQSAPI_V2
    object containing a table of monitoring agencies (MA).

Data Mart aggregate functions
-----------------------------

.. note::
    AQS Data Mart API restricts the  maximum amount of monitoring data to one
    full year of data per API call. These functions are able to return multiple
    years of data by making repeated calls to the API. Each call to the Data
    Mart API will take time to complete. The more years of data being requested
    the longer pyaqsapi will take to return the results.

These functions retrieve aggregated data from the Data Mart API and are
grouped by how each function aggregates the data. There are 5 different
families of related aggregate functions. These families are arranged by how
the Data Mart API groups the returned data, bysite, bycounty, bystate,
by<latitude/longitude bounding box> (bybox) and
by<core based statistical area> (bycbsa). Within each family
of aggregated data functions there are functions that call on the 10
different services that the Data Mart API provides. All Aggregate
functions return a pandas DataFrame by default. If the return_Header
parameter is set to True an AQSAPI_V2 object is returned instead.

These fourteen services are:

1. Monitors:
    Returns operational information about the samplers (monitors)
    used to collect the data. Includes identifying information,
    operational dates, operating organizations, etc. Functions
    using this service contain monitors in the function name.
2. Sample Data:
    Returns sample data - the most fine grain data reported to
    EPA. Usually hourly, sometimes 5-minute, 12-hour, etc.
    This service is available in several geographic selections
    based on geography: site, county, state, cbsa (core based
    statistical area, a grouping of counties), or
    by latitude/longitude bounding box. Functions using this
    service contain sampledata in the function name.
    All Sample Data functions accept two additional, optional
    parameters; cbdate and cedate.

      * cbdate:
          a date object which represents a "beginning date of last
          change" that indicates when the data was last updated.
          cbdate is used to filter data based on the change date.
          Only data that changed on or after this date will be
          returned. This is an optional variable which defaults to
          None.

      * cedate:
           a date object which represents an "end date of last change"
           that indicates when the data was last updated. cedate is
           used to filter data based on the change date. Only data
           that changed on or before this date will be returned. This
           is an optional variable which defaults to None.

      * duration:
            an optional character string that represents the parameter
            duration code that limits returned data to a specific sample
            duration. The default value of None results in no filtering
            based on duration code. Valid durations include actual sample
            durations and not calculated durations such as 8 hour
            CO or $O_3$ rolling averages, 3/6 day PM averages or
            Pb 3 month rolling averages. Refer to
            `aqs_sampledurations()`_ for a list of all available
            duration codes.

3. Daily Summary Data:
    Returns data summarized at the daily level. All daily
    summaries are calculated on midnight to midnight basis in local time.
    Variables returned include date, mean value, maximum value, etc. Functions
    using this service contain Dailysummary in the function name. All Daily
    Summary Data functions accept two additional parameters; cbdate and cedate.

      * cbdate:
          a date object which represents a "beginning date of last change"
          that indicates when the data was last updated. cbdate is used to
          filter data based on the change date. Only data that changed on or
          after this date will be returned. This is an optional variable which
          defaults to None.

      * cedate:
          a date object which represents an "end date of last change"
          that indicates when the data was last updated. cedate is
          used to filter data based on the change date. Only data
          that changed on or before this date will be returned. This
          is an optional variable which defaults to None.

4. Annual Summary Data:
    Returns data summarized at the yearly level. Variables include mean value,
    maxima, percentiles, etc. Functions using this service contain annualdata
    in the function name. All Annual Summary Data functions accept two
    additional parameters; cbdate and cedate.

      * cbdate:
           a date object which represents a "beginning date of last
           change" that indicates when the data was last updated. cbdate
           is used to filter data based on the change date. Only data
           that changed on or after this date will be returned. This is
           an optional variable which defaults to None.

      * cedate:
          a date object which represents an "end date of last change"
          that indicates when the data was last updated. cedate is used
          to filter data based on the change date. Only data that
          changed on or before this date will be returned. This is an
          optional variable which defaults to None.

5. Quarterly Summary Data:
    Returns data summarized at the quarterly level. Variables include mean
    value, maxima, percentiles, etc. Functions using this service
    contain quarterlydata in the function name. All Annual Summary Data
    functions accept two additional parameters; cbdate and cedate.

      * cbdate:
          a date object which represents a "beginning date of last change" that
          indicates when the data was last updated. cbdate is used to filter
          data based on the change date. Only data that changed on or after
          this date will be returned. This is an optional variable which
          defaults to None.

      * cedate:
          a date object which represents an "end date of last change"
          that indicates when the data was last updated. cedate is used
          to filter data based on the change date. Only data that
          changed on or before this date will be returned. This is an
          optional variable which defaults to None.

6. Quality Assurance - Blanks Data:
    Quality assurance data - blanks samples. Blanks are unexposed sample
    collection devices (e.g., filters) that are transported with the
    exposed sample devices to assess if contamination is occurring during the
    transport or handling of the samples. Functions using this service contain
    qa_blanks in the function name.

7. Quality Assurance - Collocated Assessments:
    Quality assurance data - collocated assessments. Collocated assessments
    are pairs of samples collected by different samplers at the same time
    and place. (These are "operational" samplers, assessments with
    independently calibrated samplers are called "audits".). Functions using
    this service contain qa_collocated_assessments in the function name.

8. Quality Assurance - Flow Rate Verifications:
    Quality assurance data - flow rate verifications. Several times per year,
    each PM monitor must have it's (fixed) flow rate verified by an operator
    taking a measurement of the flow rate. Functions using this service contain
    qa_flowrateverification in the function name.

9. Quality Assurance - Flow Rate Audits:
    Quality assurance data - flow rate audits. At least twice year, each PM
    monitor must have it's flow rate measurement audited by an expert using a
    different method than is used for flow rate verifications. Functions using
    this service contain qa_flowrateaudit in the function name.

10. Quality Assurance - One Point Quality Control Raw Data:
     Quality assurance data - one point quality control check raw data.
     At least every two weeks, certain gaseous monitors must be challenged with
     a known concentration to determine monitor performance. Functions using
     this service contain qa_one_point_qc in the function name.

11. Quality Assurance - pep Audits:
     Quality assurance data - performance evaluation program (pep) audits.
     Pep audits are independent assessments used to estimate total measurement
     system bias with a primary quality assurance organization. Functions
     using this service contain qa_pep_audit in the function name.

12. Transaction Sample - AQS Submission data in transaction format (RD):
     Transaction sample data - The raw transaction sample data uploaded to AQS
     by the agency responsible for data submissions in RD format. Functions
     using this service contain transactionsample in the function name.
     Transaction sample data is only available aggregated by site, county,
     state or monitoring agency.

13. Quality Assurance - Annual Performance Evaluations:
     Quality assurance data - Annual performance evaluations. A performance
     evaluation must be conducted on each primary monitor once per year. The
     percent differences between known and measured concentrations at several
     levels are used to assess the quality of the monitoring data. Functions
     using this service contain aqs_qa_annualperformanceeval in the function
     name. Annual performance in transaction format are only available
     aggregated by site, county, state, monitoring agency, and primary quality
     assurance organization. Annual performance evaluations are only available
     aggregated by site, county, state, monitoring agency, and primary quality
     assurance organization.

14. Quality Assurance - Annual performance Evaluations in transaction \
      format (RD):
      Quality assurance data - The raw transaction annual performance
      evaluations data in RD format. Functions using this service contain
      aqs_qa_annualperformanceevaltransaction in the function name. Annual
      performance evaluations in transaction format are only available
      aggregated by site, county, state, monitoring agency, and primary quality
      assurance organization.


Data Mart aggregate functions bysite
--------------------------------------
The bysite submodule exports the following functions:
::

* bysite.annualsummary,
* bysite.dailysummary,
* bysite.helperfunctions,
* bysite.monitors,
* bysite.qa_annualpeferomanceeval,
* bysite.qa_annualperformanceevaltransaction,
* bysite.qa_blanks,
* bysite.qa_collocated_assessments,
* bysite.qa_flowrateaudit,
* bysite.qa_flowrateverification,
* bysite.qa_one_point_qc,
* bysite.qa_pep_audit,
* bysite.quarterlysummary,
* bysite.sampledata,
* bysite.transactionsample

Functions exported by the bysite submodule aggregate data at the site level.
    bysite functions accept the following variables:

* parameter:
* bdate:
* edate:
* stateFIPS:
* countycode:
* sitenum:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata functions and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata functions and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).

Data Mart aggregate functions bycounty
----------------------------------------
The bycounty submodule exports the following functions:
::

* bycounty.annualsummary,
* bycounty.dailysummary,
* bycounty.helperfunctions,
* bycounty.monitors,
* bycounty.qa_annualperformanceeval,
* bycounty.qa_annualperformanceevaltransaction,
* bycounty.qa_blanks,
* bycounty.qa_collocated_assessments,
* bycounty.qa_flowrateaudit,
* bycounty.qa_flowrateverification,
* bycounty.qa_one_point_qc,
* bycounty.qa_pep_audit,
* bycounty.quarterlysummary,
* bycounty.sampledata,
* bycounty.transactionsample

Functions exported by the bycounty submodule aggregate data at the county
    level. All functions accept the following variables:

* parameter:
* bdate:
* edate:
* stateFIPS:
* countycode:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).

Data Mart aggregate functions bystate
---------------------------------------
The bystate submodule exports the following functions:
::

* bystate.annualsummary,
* bystate.dailysummary,
* bystate.helperfunctions,
* bystate.monitors,
* bystate.qa_annualperformanceeval,
* bystate.qa_annualperformanceevaltransaction,
* bystate.qa_blanks,
* bystate.qa_collocated_assessments,
* bystate.qa_flowrateaudit,
* bystate.qa_flowrateverification,
* bystate.qa_one_point_qc,
* bystate.qa_pep_audit,
* bystate.quarterlysummary,
* bystate.sampledata,
* bystate.transactionsample

Functions exported by the bystate submodule aggregate data at the state level.
    All functions accept the following variables:

* parameter:
* bdate:
* edate:
* stateFIPS:
* countycode:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).

Data Mart aggregate functions by Monitoring agency (MA)
-------------------------------------------------------
The byma submodule exports the following functions:
::

* byma.qa_annualpeferomanceeval,
* byma.qa_annualperformanceevaltransaction,
* byma.qa_blanks,
* byma.qa_collocated_assessments,
* byma.qa_flowrateaudit,
* byma.qa_flowrateverification,
* byma.qa_one_point_qc,
* byma.qa_pep_audit,
* byma.transactionsample

Functions in this family of functions aggregate data at the state level.
  All functions accept the following variables:

* parameter:
* bdate:
* edate:
* stateFIPS:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata functions and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).


Functions exported by the byma submodule aggregate data at the
    Monitoring Agency (MA) level. All functions accept the following variables:

* parameter:
* bdate:
* edate:
* MA_code:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).

Data Mart aggregate functions by Core Based Statistical Area (cbsa)
-------------------------------------------------------------------
The bycbsa submodule exports the following functions:
::

* bycbsa.annualsummary,
* bycbsa.dailysummary,
* bycbsa.helperfunctions,
* bycbsa.monitors,
* bycbsa.quarterlysummary,
* bycbsa.sampledata

Functions exported by the bycbsa submodule aggregate data at the Core Based
    Statistical Area (cbsa, as defined by the US Census Bureau) level.
    All functions accept the following variables:

* parameter:
* bdate:
* edate:
* cbsa_code:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).


Data Mart aggregate functions by Primary Quality Assurance Organization (pqao)
------------------------------------------------------------------------------
The bypqao submodule exports the following functions:
::

* bypqao.qa_annualperformanceeval,
* bypqao.qa_annualperformanceevaltransaction,
* bypqao.qa_blanks,
* bypqao.qa_collocated_assessments,
* bypqao.qa_flowrateaudit,
* bypqao.qa_flowrateverification,
* bypqao.qa_one_point_qc,
* bypqao.qa_pep_audit

Functions exported by the bypqao submodule aggregate data at the
    Primary Quality Assurance Organization (pqao) level. All functions accept
    the following variables:

* parameter:
* bdate:
* edate:
* pqao_code:
* return_header (optional): set to False by default.

Data Mart aggregate functions by latitude/longitude bounding box (bybox)
--------------------------------------------------------------------------
The bybox submodule exports the following functions:
::

* bybox.annualsummary,
* bybox.dailysummary,
* bybox.helperfunctions,
* bybox.monitors,
* bybox.quarterlysummary,
* bybox.sampledata

Functions exported by the bybox submodule aggregate data by a
    latitude/longitude bounding box (bybox) level. All functions accept the
    following variables:

* parameter:
* bdate:
* edate:
* minlat:
* minlon:
* maxlon:
* maxlat:
* cbdate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* cedate (optional):
    (This parameter is only used in conjunction with sampledata, dailysummary,
    annualdata and quarterlysummary functions).
* return_header (optional):
    set to False by default.
* duration (optional):
    (This parameter is only used in conjunction with sampledata functions).

pyaqsapi Miscellaneous functions
--------------------------------

These are miscellaneous functions exported by pyaqsapi.

aqs_removeheader is the function that the pyaqsapi library
uses internally to coerce an AQSAPI_V2 object into a pandas DataFrame.
This is useful if the user saves the output from another pyaqsapi function
with return_header = True set but later decides that they want just a
simple pandas DataFrame object. This function takes only one variable:

* AQSobject:
