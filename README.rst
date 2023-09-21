.. meta::
   :description: A simple interface to the US Environmental Protection Agency's
       (US EPA) Air quality System (AQS) Data Mart API.
   :keywords: pyaqsapi, RAQSAPI, USEPA, ambient air monitoring, AQS, Data Mart

.. note::
    This software/application was developed by the U.S. Environmental
    Protection Agency (USEPA). No warranty expressed or implied is made
    regarding the accuracy or utility of the system, nor shall the act of
    distribution constitute any such warranty. The USEPA has relinquished
    control of the information and no longer has responsibility to protect the
    integrity, confidentiality or availability of the information. any
    reference to specific commercial products, processes, or services by
    service mark, trademark, manufacturer, or otherwise, does not constitute or
    imply their endorsement, recommendation or favoring by the USEPA.
    The USEPA seal and logo shall not be used in any manner to imply
    endorsement of any commercial product or activity by the USEPA or the
    United States Government.

.. warning::
    US EPA’s AQS Data Mart API V2 is currently in beta phase of development,
    the API interface has not been finalized. This means that certain
    functionality of the API may change or be removed without notice. As a
    result, this package is also currently marked as beta and may also change
    to reflect any changes made to the Data Mart API or in respect to
    improvements in the design, functionality, quality and documentation of
    this package. The authors assume no liability for any problems that may
    occur as a result of using this package, the Data Mart service, any
    software, service, hardware, or user accounts that may utilize this
    package.

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: This repository uses black for code formatting
    :align: center
.. image:: https://img.shields.io/github/workflow/status/USEpa/pyaqsapi/build_and_test_pyaqsapi_on_ubuntu?style=plastic
   :alt: GitHub Workflow Status
   :align: center
.. image:: https://img.shields.io/github/issues/USEpa/pyaqsapi?style=plastic
    :target: https://github.com/USEPA/pyaqsapi/issues
    :alt: GitHub issues
    :align: center
.. image:: https://img.shields.io/github/license/USEPA/pyaqsapi?style=plastic
    :target: https://github.com/USEPA/pyaqsapi/blob/main/LICENSE.rst
    :alt: MIT License
    :align: center
.. image:: https://github.com/USEPA/pyaqsapi/workflows/build_and_test_pyaqsapi_on_ubuntu/badge.svg
    :target: https://github.com/USEPA/pyaqsapi/actions/workflows/github-ubuntu.yaml
    :alt: Github actions
    :align: center  

============
Introduction
============
The pyaqsapi module for the python 3 programming environment allows a python 3
programming environment to connect to and retrieve data from the United States
Environmental Protection Agency’s (US EPA) Air Quality System (AQS) Data Mart
API v2 (Air Quality System)1 interface directly. This package enables the data
user to omit legacy challenges including coercing data from a JSON object to a
usable python 3 object, retrieving multiple years of data, formatting API
requests, retrieving results, handling credentials, requesting multiple
pollutant data and rate limiting data requests. All the basic functionality
of the API have been implemented that are available from the AQS API Data Mart
server. The library connects to AQS Data Mart API via Hypertext Transfer
Protocol (HTTP) so there is no need to install external ODBC drivers, configure
ODBC connections or deal with the security vulnerabilities associated with
them. Most functions have a parameter, return_header which by default is set
to FALSE. If the user decides to set return_header to TRUE, then that function
will return a python 3 AQS_DATAMART_APIv2 object. An AQS_DATAMART_APIv2 object
has instance methods for retrieving the data requested, header information,
and other metadata related to the API call. After each call to the API a five
second stall is invoked to help prevent overloading the Data Mart API server
and to serve as a simple rate limit.

RAQSAPI
=======
pyaqsapi is a port of `RAQSAPI`_ to the python 3 programming environment. For
anyone that is familiar with RAQSAPI, the pyaqsapi API will feel familiar to you,
most of the functions are similar and the parameters sent to each functions
are the same. pyaqsapi aims to have feature parity with RAQSAPI and neither
project will have features that the other project doesn't - other than
programming language environment or language preference there is no benefit to
using one package over the other.

Install pyaqsapi
----------------
To install pyaqsapi first clone the pyaqsapi repository.

.. code-block:: console

    git clone https://github.com/USEPA/pyaqsapi.git

Next, use pip to install the proper dependencies that are required to build
and install pyaqsapi.

.. code-block:: bash

    pip install -r requirements.txt

Next change into the new directory then use setuptools to build and pip
to install the package.

.. code-block:: bash

    cd pyaqsapi
    python -m build .
    python -m pip install .

Load pyaqsapi
=============
Like any other python package make sure that you are loading pyaqsapi in the
same virtual environment where pyaqsapi was installed. Load pyaqsapi in the
same any other python package is loaded.

.. code-block:: python3

   import pyaqsapi as aqs

Using pyaqsapi
==============
For those who are already familiar with using RAQSAPI then the pyaqsapi API
should feel familiar with a few minor differences regarding how the data is
returned.

All data is returned using pandas Data Frames. Exported functions from pyaqsapi
have a parameter RETURN_HEADER, by default this parameter is False. When False
these functions simply return the requested data as a pandas Data Frame. If
RETURN_HEADER is manually set to True an AQSAPI_V2 python 3 object is returned.
Use the get_data() class method to retrieve the data, get_header() class
method to retrieve header information.

Sign up and setting up user credentials with the RAQSAPI library
================================================================
If you have not already done so you will need to sign up with AQS Data Mart
using aqs_sign_up function,[2] this function takes one input, “email,” which
is a python 3 character object, that represents the email address that you want
to use as a user credential to the AQS Data Mart service. After a successful
call to aqs_sign_up an email message will be sent to the email address provided
with a new Data Mart key which will be used as a credential key to access the
Data Mart API. The aqs_sign_up function can also be used to regenerate a new
key for an existing user, to generate a new key simply call the aqs_sign_up
function with the parameter “email” set to an existing account. A new key will
be e-mailed to the account given.

The credentials used to access the Data Mart API service are stored in as a
python global variable that needs to be set every time the pyaqsapi module is
loaded or the key is changed. Without valid credentials, the Data Mart server
will reject any request sent to it. The key used with Data Mart is a key and is
not a password, so the pyaqsapi package does not treat the key as a password;
this means that the key is stored in plain text and there are no attempts to
encrypt Data Mart credentials as would be done for a username and password
combination. The key that is supplied to use with Data Mart is not intended for
authentication but only account monitoring. Each time pyaqsapi is loaded and
before using any of it’s functions use the aqs_credentials function to enter in
the user credentials so that pyaqsapi can access the AQS Data Mart server.

.. note::
    The credentials used to access AQS Data Mart API are not the same as the
    credentials used to access AQS. AQS users who do not have access to the
    AQS Data Mart will need to create new credentials. However, you may use the
    same credentials used in RAQSAPI in pyaqsapi since RAQSAPI ewes the the same
    AQS Data Mart API as pyaqsapi.

Data Mart aggregate functions
-----------------------------
These functions retrieve aggregated data from the Data Mart API and are grouped
by how each function aggregates the data. There are 7 different families of
related aggregate functions in which the AQS Data Mart API groups data.

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
      (\*qa_annualPeferomanceeval)
    - \ Quality Assurance - Annual Performance Evaluations in the AQS
      (\*qa_annualpeferomanceeval)
    - \ Submission transaction format (RD)
      (\*qa_annualpeferomanceevaltransaction)

.. note::
    AQS Data Mart API restricts the maximum amount of monitoring data to one
    full year of data per API call. These functions are able to return multiple
    years of data by making repeated calls to the API. Each call to the Data
    Mart API will take time to complete. The more years of data being requested
    the longer RAQSAPI will take to return the results.
    
Read the full 
`API documentation <https://usepa.github.io/pyaqsapi/>`_ online.


Aggregate functions are named aqs.<aggregation>.<service>() where <service>
is one of the 13 services listed above and <aggregation> is either
"bysite“, ”bycounty“, ”bystate“, ”bybox“, ”bycbsa", "byma" or "bypqao".
