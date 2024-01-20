.. index:: pyaqsapi aggregate functions (brief)

Data Mart aggregate functions
=============================
.. note::
    AQS Data Mart API restricts the maximum amount of monitoring data to one
    full year of data per API call. These functions are able to return multiple
    years of data by making repeated calls to the API. Each call to the Data
    Mart API will take time to complete. The more years of data being requested
    the longer pyaqsapi will take to return the results.

These functions retrieve aggregated data from the Data Mart API and are grouped
by how each function aggregates the data. There are 7 different families of
related aggregate functions in which the AQS Data Mart API groups data.

.. index:: aggregate functions

These seven families are:

   - by site (aqs.bysite)
   - by county (aqs.bycounty)
   - by state (aqs.bystate)
   - by latitude/longitude bounding box (aqs.bybox)
   - by monitoring agency (aqs.byma)
   - by Primary Quality Assurance Organization (aqs.bypqao)
   - by core based statistical area (as defined by the US census Bureau)
     (aqs.bycbsa).

Within these families of aggregated data functions there are functions that
call on the 13 different aggregate services that the Data Mart API provides.
Note that not all aggregations are available for each service.

.. index:: services

These thirteen services are:

    - \ Monitors (\*monitors)
    - \ Sample Data (\*sampledata)
    - \ Daily Summary Data (\*dailydata)
    - \ Annual Summary Data (annualdata)
    - \ Quality Assurance - Blanks Data (\*qa_blanks)
    - \ Quality Assurance - Collocated Assessments
      (\*qa_collocated_assessments)
    - \ Quality Assurance - Flow Rate Verifications (\*qa_flowrateverification)
    - \ Quality Assurance - Flow Rate Audits (\*aqs_qa_flowrateaudit)
    - \ Quality Assurance - One Point Quality Control Raw Data
      (\*qa_one_point_qc)
    - \ Quality Assurance - PEP Audits (\*qa_pep_audit)
    - \ Transaction Sample - AQS Submission data in transaction Format (RD)
      (\*transactionsample)
    - \ Quality Assurance - Annual Performance Evaluations
      (\*qa_annualpeferomanceeval)
    - \ Quality Assurance - Annual Performance Evaluations in the AQS
      \ Submission transaction format (RD)
      \ (\*qa_annualpeferomanceevaltransaction)


Aggregate functions are named aqs.<aggregation>.<service>() where <service>
is one of the 13 services listed above and <aggregation> is either
"bysite“, ”bycounty“, ”bystate“, ”bybox“, ”bycbsa", "byma" or "bypqao".