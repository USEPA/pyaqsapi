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
