.. meta::
   :description: A simple interface to the US Environmental Protection Agency's
       (US EPA) Air quality System (AQS) Data Mart API.
   :keywords: pyaqsapi, RAQSAPI, USEPA, ambient air monitoring, AQS, Data Mart

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=plastic
    :target: https://github.com/psf/black
    :alt: This repository uses black for code formatting
    :align: center
.. image:: https://img.shields.io/github/issues/USEpa/pyaqsapi?style=plastic
    :target: https://github.com/USEPA/pyaqsapi/issues
    :alt: GitHub issues
    :align: center
.. image:: https://img.shields.io/github/license/USEPA/pyaqsapi?style=plastic
    :target: https://github.com/USEPA/pyaqsapi/blob/main/LICENSE.rst
    :alt: MIT License
    :align: center
.. image:: https://img.shields.io/github/actions/workflow/status/USEPA/pyaqsapi/.github%2Fworkflows%2Fbuild/\
           andtestpyaqsapi.yml?style=plastic
   :alt: GitHub Workflow Status (with event)
   :target: https://github.com/USEPA/pyaqsapi/actions/workflows/github-ubuntu.yaml
   :align: center
.. image:: https://img.shields.io/github/last-commit/USEpa/pyaqsapi?style=plastic
   :alt: GitHub last commit
   :target: https://github.com/USEPA/pyaqsapi
   :align: center
.. image:: https://img.shields.io/pypi/dm/pyaqsapi?style=plastic
   :alt: PyPI - Downloads
   :target: https://pypi.org/project/pyaqsapi/
   :align: center
.. image:: https://img.shields.io/github/license/USEpa/pyaqsapi?style=plastic
   :alt: GitHub License
   :align: center
   :target: https://pypi.org/project/pyaqsapi/ https://github.com/USEPA/pyaqsapi/blob/main/LICENSE.rst
.. image:: https://img.shields.io/pypi/v/pyaqsapi?style=plastic
   :alt: PyPI - version
   :align: center
   :target:  https://pypi.org/project/pyaqsapi/
.. image:: https://img.shields.io/conda/vn/conda-forge/pyaqsapi.svg?style=plastic
   :alt: Conda-forge - version
   :align: center
   :target: https://github.com/conda-forge/pyaqsapi-feedstock/


EPA Disclaimer
==============

.. note::
    This software/application was developed by the U.S. Environmental
    Protection Agency (USEPA). No warranty expressed or implied is made
    regarding the accuracy or utility of the system, nor shall the act of
    distribution constitute any such warranty. The USEPA has relinquished
    control of the information and no longer has responsibility to protect
    the integrity, confidentiality or availability of the information. Any
    reference to specific commercial products, processes, or services by
    service mark, trademark, manufacturer, or otherwise, does not constitute
    or imply their endorsement, recommendation or favoring by the USEPA. The
    USEPA seal and logo shall not be used in any manner to imply endorsement
    of any commercial product or activity by the USEPA or the United States
    Government.

AQS Data Mart Disclaimer
========================

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

Introduction
============
The ``pyaqsapi`` module for the python 3 programming environment allows a
python 3 programming environment to connect to and retrieve data from the
United States Environmental Protection Agency\’s (US EPA) Air Quality System
(AQS) Data Mart API v2 (Air Quality System) interface directly. This package
enables the data user to omit legacy challenges including coercing data from a
JSON object to a usable python 3 object, retrieving multiple years of data,
formatting API requests, retrieving results, handling credentials, requesting
multiple pollutant data and rate limiting data requests. All the basic
functionality of the API have been implemented that are available from the AQS
API Data Mart server. The library connects to AQS Data Mart API via Hypertext
Transfer Protocol (HTTP) so there is no need to install external ODBC drivers,
configure ODBC connections or deal with the security vulnerabilities associated
with them. Most functions have a parameter, ``return_header`` which by default
is set to ``FALSE``. If the user decides to set ``return_header`` to ``TRUE``,
then that function will return a python 3 ``AQSAPI_V2`` object. An ``AQSAPI_V2``
object has instance methods for retrieving the data requested, header
information, and other metadata related to the API call. After each call to the
API a five second stall is invoked to help prevent overloading the Data Mart API
server and to serve as a simple rate limit.

About the timeliness of AQS Data
================================

EPA's AQS Data Mart API, the service that ``pyaqsapi`` retrieves data from, does
not host real time (collected now/today) data. If real time data is needed,
please use the AirNow API and direct all questions toward real time data there.
``pyaqsapi`` does not work with AirNow and cannot retrieve real time data.
For more details see section 7.1 of the About AQS Data page.

About ``RAQSAPI``
=================
``pyaqsapi`` is a port of `RAQSAPI <https://github.com/USEpa/RAQSAPI>`_ to the
python 3 programming environment. For anyone that is familiar with ``RAQSAPI``,
the pyaqsapi API will feel familiar to you, most of the functions are similar
and the parameters sent to each functions are the same. pyaqsapi aims to have
feature parity with ``RAQSAPI`` and neither project will have features that the
other project does not - other than programming language environment or
language preference there is no benefit to using one package over the other.

Install pyaqsapi
================
The user has the choice of installing pyaqspi as a precompiled binary or from either
pypi or conda-forge or installing from source.

Packaged Binary install options (preferred method)
--------------------------------------------------
Most users should install pyaqsapi using one of the packaged binary install options below.

Packaged binary install of pyaqsapi from pypi.org using pip or `uv <https://github.com/astral-sh/uv>`_
--------------------------------------------------------------------------------------------------------
.. code-block:: console

   pip install pyaqsapi

   # List `pyaqsapi` metadata using pip:
   pip show pyaqsapi

   Alternatively, (uv)[https://github.com/astral-sh/uv] can be used as an alternative to pip by replacing the command
   `pip` with `uv pip` if `uv` is installed


Packaged binary install of pyaqsapi from `conda-forge <https://conda-forge.org/>`_ using conda or `mamba <https://github.com/mamba-org/mamba>`_
-----------------------------------------------------------------------------------------------------------------------------------------------
Installing pyaqsapi from the conda-forge channel can be achieved by adding conda-forge to your channels with:
.. code-block:: console

  conda config --add channels conda-forge
  conda config --set channel_priority strict

Once the conda-forge channel has been enabled, pyaqsapi can be installed with conda:
.. code-block:: console

  conda install pyaqsapi

mamba can be used as an alternative to conda:
.. code-block:: console

  mamba config --add channels conda-forge
  mamba --set channel_priority strict
  mamba install pyaqsapi

It is possible to list all of the versions of pyaqsapi available on your platform:
.. code-block:: console

  conda/mamba search pyaqsapi --channel conda-forge

Alternatively, conda/mamba repoquery may provide more information:
.. code-block:: console

  # Search all versions available on your platform:
  {conda/mamba} repoquery search pyaqsapi --channel conda-forge

  # List dependencies of `pyaqsapi`:
  {conda/mamba} repoquery depends pyaqsapi --channel conda-forge


Install pyaqsapi from source (manual install from github)
---------------------------------------------------------
To install pyaqsapi first clone the pyaqsapi repository.

.. code-block:: console

   git clone https://github.com/USEPA/pyaqsapi.git

Next, in the project's root directory use pip to install the proper
dependencies that are required to build
and install pyaqsapi.

.. code-block:: console

    pip install -r requirements.txt

While still in the project's root directory use setuptools to build and pip
to install the package.

.. code-block:: console

    python -m build .
    python -m pip install .


Using ``pyaqsapi``
==================
For those who are already familiar with using ``RAQSAPI`` then the ``pyaqsapi`` API
should feel familiar with a few minor differences regarding how the data is
returned.

All data is returned using pandas DataFrames. Exported functions from ``pyaqsapi``
have a parameter ``RETURN_HEADER``, by default this parameter is ``False``. When ``False``
these functions simply return the requested data as a pandas DataFrame. If
``RETURN_HEADER`` is manually set to ``True`` an ``AQSAPI_V2`` python 3 object is returned.
Use the ``get_data()`` class method to retrieve the data, ``get_header()`` class
method to retrieve header information.

Sign up and setting up user credentials with the ``pyaqsapi`` library
=====================================================================
If you have not already done so you will need to sign up with AQS Data Mart
using ``aqs_sign_up`` function, this function takes one input, ``email``, which
is a python 3 character object, that represents the email address that you want
to use as a user credential to the AQS Data Mart service. After a successful
call to ``aqs_sign_up`` an email message will be sent to the email address provided
with a new Data Mart key which will be used as a credential key to access the
Data Mart API. The ``aqs_sign_up`` function can also be used to regenerate a new
key for an existing user, to generate a new key simply call the ``aqs_sign_up``
function with the parameter ``email`` set to an existing account. A new key will
be e-mailed to the account given.

The credentials used to access the Data Mart API service are stored in as a
python global variable that needs to be set every time the ``pyaqsapi`` module is
loaded or the key is changed. Without valid credentials, the Data Mart server
will reject any request sent to it. The key used with Data Mart is a key and is
not a password, so the ``pyaqsapi`` package does not treat the key as a password;
this means that the key is stored in plain text and there are no attempts to
encrypt Data Mart credentials as would be done for a username and password
combination. The key that is supplied to use with Data Mart is not intended for
authentication but only account monitoring. Each time ``pyaqsapi`` is loaded and
before using any of it’s functions use the ``aqs_credentials`` function to enter
in the user credentials so that ``pyaqsapi`` can access the AQS Data Mart
server.

Both ``pyaqsapi`` and ``RAQSAPI`` use the US Environmental Protection Agency\'s
Air Quality Service Data Mart to retrieve data. The same credentials can be used
for access to either project. Note however, that AQS and AQS Data Mart are
similar and related data sources, however the credentials used to access AQS are
not the same as those used to access AQS Data Mart.

.. note::
    The credentials used to access AQS Data Mart API are not the same as the
    credentials used to access AQS. AQS users who do not have access to the
    AQS Data Mart will need to create new credentials. However, you may use the
    same credentials used in ``RAQSAPI`` in ``pyaqsapi`` since ``RAQSAPI`` uses
    the same AQS Data Mart API as ``pyaqsapi``.


Data Mart aggregate functions
=============================
.. note::
    AQS Data Mart API restricts the maximum amount of monitoring data to one
    full year of data per API call. These functions are able to return multiple
    years of data by making repeated calls to the API. Each call to the Data
    Mart API will take time to complete. The more years of data being requested
    the longer ``pyaqsapi`` will take to return the results.

These functions retrieve aggregated data from the Data Mart API and are grouped
by how each function aggregates the data. There are 7 different families of
related aggregate functions in which the AQS Data Mart API groups data.

These seven families are:

- by site (``aqs.bysite``)
- by county (``aqs.bycounty``)
- by state (``aqs.bystate``)
- by latitude/longitude bounding box (``aqs.bybox``)
- by monitoring agency (``aqs.byma``)
- by Primary Quality Assurance Organization (``aqs.bypqao``)
- by core based statistical area (as defined by the US census Bureau)
  (``aqs.bycbsa``).

Within these families of aggregated data functions there are functions that
call on the 13 different aggregate services that the Data Mart API provides.
Note that not all aggregations are available for each service.

These thirteen services are:

- Monitors (``*monitors``)
- Sample Data (``*sampledata``)
- Daily Summary Data (``*dailydata``)
- Annual Summary Data (``annualdata``)
- Quality Assurance - Blanks Data (``*qa_blanks``)
- Quality Assurance - Collocated Assessments (``*qa_collocated_assessments``)
- Quality Assurance - Flow Rate Verifications (``*qa_flowrateverification``)
- Quality Assurance - Flow Rate Audits (``*aqs_qa_flowrateaudit``)
- Quality Assurance - One Point Quality Control Raw Data (``*qa_one_point_qc``)
- Quality Assurance - PEP Audits (``*qa_pep_audit``)
- Transaction Sample - AQS Submission data in transaction Format (RD) (``*transactionsample``)
- Quality Assurance - Annual Performance Evaluations (``*qa_annualpeferomanceeval``)
- Quality Assurance - Annual Performance Evaluations in the AQS Submission transaction format (RD) (``*qa_annualpeferomanceevaltransaction``)


Aggregate functions are named ``aqs.<aggregation>.<service>()`` where ``<service>``
is one of the 13 services listed above and ``<aggregation>`` is either
``bysite``, ``bycounty``, ``bystate``, ``bybox``, ``bycbsa``, ``byma`` or ``bypqao``.


Read the full
`documentation <https://usepa.github.io/pyaqsapi/>`_ online.

