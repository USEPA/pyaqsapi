.. index:: Introduction;
.. sectionauthor:: Clinton Mccrowey \<mccrowey \<DOT\>\ clinton \<AT\>\ epa.gov\>

Introduction
============
The pyaqsapi package for the python 3 programming environment allows a python 3
programming environment to connect to and retrieve data from the United States
Environmental Protection Agency’s (US EPA) Air Quality System (AQS) Data Mart
API v2 (Air Quality System) :cite:t:`AQSDataMartWelcome` interface directly.
This package enables the data user to omit legacy challenges including coercing
data from a JSON object to a usable python 3 object, retrieving multiple years
of data, formatting API requests, retrieving results, handling credentials,
requesting multiple pollutant data and rate limiting data requests.
All the basic functionality of the API have been implemented that are available
from the AQS API Data Mart server. The library connects to AQS Data Mart API
via Hypertext Transfer Protocol (HTTP) so there is no need to install external
ODBC drivers, configure ODBC connections or deal with the security
vulnerabilities associated with them. Most functions have a parameter,
return_header which by default is set to FALSE. If the user decides to
set return_header to TRUE, then that function will return a python 3
AQSAPI_V2 object. An AQSAPI_V2 object has instance methods for retrieving the
data requested, header information, and other metadata related to the API call.
After each call to the API a five second stall is invoked to help prevent
overloading the Data Mart API server and to serve as a simple rate limit.

The Air Quality System (AQS)
----------------------------
The Clean Air act :cite:t:`cleanairact` requires all federal, state, local and
tribal air pollution control agencies monitor ambient air for concentrations of
certain air pollutants. Codified in 40 CFR Part 58 are the statutory
requirements for these monitoring programs, including monitoring network
technical requirements, operating schedules, data certification, data submittal
and archiving requirements. In addition to the required air pollution and
meteorological monitoring, pollution control agencies often perform additional
and/or voluntary air monitoring.

* The three objectives of ambient air monitoring programs as stated in 40 CFR
      Part 58 Appendix D.1 are as follows:

    * Provide air pollution data to the public in a timely manner;
    * Support compliance with ambient air quality standards and emissions
      strategy development; and
    * Support for air pollution research studies.

As required by 40 CFR Part 58, air pollution and meteorological data is
submitted to the United States Environmental Protection Agency along with
associated metadata and quality assurance metadata via EPA's Air
Quality System (AQS):cite:t:`@AboutAQSdata`.

About AQS Data Mart
-------------------
AQS Data Mart is a publicly accessible mirror of data stored on the AQS database
designed to make air monitoring data more accessible and useful to the technical
community, scientific community and the general public. Data on AQS is copied to
AQS Data Mart once per week and this data is made available to the public
through web-based applications and APIs (application programming interface)
:cite:t:`AQSDataMartWelcome`. pyaqsapi functions use the APIs provided by AQS
Data Mart to retrieve data.