:orphan:

.. index:: Using pyaqsapi
.. sectionauthor:: Clinton Mccrowey \<mccrowey \<DOT\>\ clinton \<AT\>\ epa.gov\>

Using pyaqsapi
==============
For those who are already familiar with using :cite:t:`Rpackage:RAQSAPI`
RAQSAPI then the pyaqsapi API should feel familiar with a few minor differences
regarding how the data is returned.

By default data is returned as a pandas Data Frames :cite:t:`pandas_DataFrame`.
Exported functions from pyaqsapi have a parameter RETURN_HEADER, by default
this parameter is False. When False functions simply return the requested
data as a pandas Data Frame. If RETURN_HEADER is manually set to True a list of
AQSAPI_V2 python 3 objects are returned. Use the get_data() class method to
retrieve the data and the get_header() class method to retrieve header
information.

.. index:: sign_up

Sign up and setting up user credentials with the pyaqsapi library
=================================================================
If you have not already done so you will need to sign up with AQS Data Mart
using aqs_sign_up function, this function takes one input, “email,” which
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

Both pyaqsapi and RAQSAPI use the US Environmental Protection Agency's Air
Quality Service DataMart to retrieve data. The same credentials can be used for 
access to either project. Note however, that AQS and AQS DataMart are similar
and related data sources, however the credentials used to access AQS are not the
same as those used to access AQS DataMart.

.. note::
    The credentials used to access AQS Data Mart API are not the same as the
    credentials used to access AQS. AQS users who do not have access to the
    AQS Data Mart will need to create new credentials. However, you may use the
    same credentials used in RAQSAPI in pyaqsapi since RAQSAPI ewes the the same
    AQS Data Mart API as pyaqsapi.
