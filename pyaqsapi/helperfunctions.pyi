# pylint: skip-file 

from datetime import date
from pandas import DataFrame
from ratelimit import sleep_and_retry
from typing import Any, no_type_check

AQS_user: str | None
AQS_key: str | None
ONE_MINUTE: int

class AQSAPI_V2:
    """AQSAPI_V2 class used to store and retrieve data from the EPA AQS Datamart API.

    Attributes
    ----------
    _header (pandas DataFrame): header information returned from the
        AQS Datamart API.
    _request_time (str): the time stamp that the call to the AQS Datamart
        API was received.
    _status (str): the status (associated with the _status_code) returned
        from a call to the AQS Datamart API.
    _status_code (str): the numeric status_code (represented as a string)
        that is returned from a call to the AQS Datamart API.
    _rows (str): the number of rows contained in the _data.
    _url (str): a string representing the URL used to make the AQS Datamart
        API call.
    _data (pandas DataFrame): the data returned from a call to the
        AQS Datamart API.

    Methods
    -------
    set_data():
    set_header():
    get_data():
    get_header():
    get_status_code():
    get_header():
    get_url():
    get_header():
    get_request_time():
    get_status()
    get_numberofrows()
    """
    _header: DataFrame
    _data: DataFrame
    _request_time: str | None
    _rows: int | None
    _url: str | None
    _status_code: str | None
    _status: str | None
    _numberofrows: int | None
    def __init__(self) -> None:
        """Initiate the AQSAPI_V2 instance."""
    def set_header(self, Header: DataFrame) -> None:
        """Set the header of a single AQSAPI_V2 object. Header must be a pandas DataFrame.

        Warns
        -----
        UserWarning
            A warning is thrown if Header is not a pandas DataFrame

        Parameters
        ----------
        Header : Pandas DataFrame
            A pandas.DataFrame instance with the header information.

        Returns
        -------
        None.

        """
    def get_request_time(self) -> str:
        """Retrieve the time that the request to the AQS DataMart API was made.

        Returns
        -------
        (str) A string representing the time that that request to the AQS
        DataMart API was made.

        """
    def get_numberofrows(self) -> int:
        """Retrieve the number of rows of data returned from the API call.

        This information can be used to track the amount of data requested.

        Returns
        -------
        (int) An int representing the number of rows of data returned from the API call.

        """
    def get_data(self) -> DataFrame:
        """Return the Data portion of the AQSAPI_V2 instance.

        Returns
        -------
        (pandas DataFrame) a DataFrame containing the Data portion of the
        AQSAPI_V2 instance.

        """
    def set_data(self, Data: DataFrame) -> None:
        """Set the Data of a single AQSAPI_V2 object. Data must be a pandas DataFrame.

        Raises
        ------
        UserWarning
            A warning is thrown if Data is not a pandas DataFrame

        Returns
        -------
        None

        """
    def get_header(self) -> DataFrame:
        """Return the Header portion of the AQSAPI_V2 instance.

        Returns
        -------
        (pandas DataFrame) a DataFrame containing the Header portion of the
        AQSAPI_V2 instance.

        """
    def get_status_code(self) -> str:
        """Retrieve the status code from the API call.

        Returns
        -------
        (str) A string representing the status code returned from the EPA
        DataMart API.

        """
    def get_url(self) -> str:
        """Retrieve the URL of the AQS DataMart API request.

        Returns
        -------
        (str) A string representing the status code returned from the EPA
        DataMart API.

        """
    def get_status(self) -> str:
        """Retrieve the status message from the API call.

        Returns
        -------
        (str) A string representing the status message returned from the EPA
        DataMart API.

        """
    def _set_status(self, status: str) -> None:
        """Set the status message of the AQS DataMart API call.

        Parameters
        ----------
        status : str
                 A string representing the API call's status message.

        Returns
        -------
        None

        """
    def _set_numberofrows(self, numberofrows: int) -> None:
        """Set the number of rows of data returned from the API call.

        Parameters
        ----------
        numberofrows : int
                       A integer representing the number of rows of data returned.

        Returns
        -------
        None

        """
    def _set_status_code(self, status_code: str) -> None:
        """Set the status code of the AQS DataMart API call.

        Parameters
        ----------
        status_code : str
                      A string representing the status code

        Returns
        -------
        None

        """
    @no_type_check
    @sleep_and_retry
    def __aqs(self, service=None, aqsfilter=None, variables=None, AQS_user=None, key=None, AQS_domain: str = 'https://aqs.epa.gov/data/api'):
        """Send AQS request to the AQS API and returns the result.

        This helper method is used to abstract the call to AQS API away from functions that need it's result.
        This helper method is not meant to be called directly from external functions.

        Parameters
        ----------
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        aqsfilter : str
                    a string which represents the filter used in conjunction with
                    the service requested. For a list of available services
                    and filters see
                 https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        variables : dict
                    A python dictionary of containing key-value pairs of
                    variables to be sent to the AQS DataMart API.
        AQS_user : str
                   A python character object which represents the email account
                   that will be used to authenticate with the AQS API.
        key : str
              The key associated with the AQS_user account represented as a
              character string.
        AQS_domain : str
                     The base domain for the url used in API requests. Normally
                     this should be set to <https://aqs.epa.gov/data/api/>,
                     this parameter allows the domain to be overridden.

        Returns
        -------
        (AQSAPI_v2) An AQSAPI_V2 instance containing the data requested.

        """
    def _aqs_services_by_site(self, parameter: str, bdate: date, edate: date, stateFIPS: str, countycode: str, sitenum: str, service: str, duration: str | None = None, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the bysite service.

        This is a helper method and should not be called by the end user. A helper method used by bysite functions
        to call the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        stateFIPS : str
                    a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        countycode : str
                    a python character object which represents the 3 digit
                    state FIPS code for the county being requested
                    (with leading zero(s)). Use aqs_counties_by_state() for
                    the list of available county codes for each state.
        sitenum : str
                  a python character object which represents the 4 digit site
                  number (with leading zeros) within the county and state
                  being requested.
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : str, optional
                   an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : datetime.date
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        '''
    def _aqs_services_by_county(self, parameter: str, bdate: date, edate: date, stateFIPS: str, countycode: str, service: str, duration: str | None = None, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the bycounty service.

        This is a helper method and should not be called by the end user. This method is used by bycounty functions
        to call the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        stateFIPS : str
                    a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        countycode : str
                    a python character object which represents the 3 digit
                    state FIPS code for the county being requested
                    (with leading zero(s)). Use aqs_counties_by_state() for
                    the list of available county codes for each state.
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : str, optional
                   an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : datetime.date, optional
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date, optional
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        '''
    def _aqs_services_by_state(self, parameter: str, bdate: date, edate: date, stateFIPS: str, service: str, duration: str | None = None, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the bystate service.

        This is a helper method and should not be called by the end user. This method is used by bystate functions to
        call the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        stateFIPS : str
                    a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : str, optional
                   an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : datetime.date, optional
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date, optional
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        '''
    def _aqs_services_by_box(self, parameter: str, bdate: date, edate: date, minlat: str, maxlat: str, minlon: str, maxlon: str, service: str, duration: str | None = None, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the bybox service.

        This is a helper method and should not be called by the end user. This method is used by bybox functions to call
        the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        minlat : str
                 a python character object which represents the minimum
                 latitude of a geographic box. Decimal latitude with north
                 begin positive. Only data north of this latitude will be
                 returned.
        maxlat : str
                 a python character object which represents the maximum
                 latitude of a geographic box. Decimal latitude with north
                 begin positive. Only data south of this latitude will be
                 returned.
        minlon : str
                 a python character object which represents the minimum
                 longitude of a geographic box. Decimal longitude with east
                 begin positive. Only data east of this longitude will be
                 returned.
        maxlon : str
                 a python character object which represents the maximum
                 longitude of a geographic box. Decimal longitude with east
                 begin positive. Only data west of this longitude will be
                 returned. Note that -80 is less than -70.
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : str, optional
                   an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : datetime.date, optional
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date, optional
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        '''
    def _aqs_services_by_cbsa(self, parameter: str, bdate: date, edate: date, cbsa_code: str, service: str, duration: str | None = None, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the bycbsa service.

        This is a helper method and should not be called by the end user. This method is used by bycbsa functions to
        call the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        cbsa_code: str
                   a python character object which represents the 5 digit AQS
                   Core Based Statistical Area code (the same as the census
                   code, with leading zeros).
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : str, optional
                   an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : datetime.date, optional
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date, optional
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        '''
    def _aqs_services_by_pqao(self, parameter: str, bdate: date, edate: date, pqao_code: str, service: str, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the bypqao service.

        This is a helper method and should not be called by the end user. This method is used by bypqao functions to call
        the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        pqao_code : str
                    a python character object which represents the 4 digit AQS
                    Primary Quality Assurance Organization code
                    (with leading zeroes).
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : str, optional
                   an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : datetime.date, optional
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date, optional
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.
        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        '''
    def _aqs_services_by_MA(self, parameter: str, bdate: date, edate: date, MA_code: str, service: str, cbdate: date | None = None, cedate: date | None = None) -> DataFrame | None:
        '''Call _aqs for functions using the byMonitoring Agency (MA) service.

        This is a helper method and should not be called by the end user. This method is used by byma functions to call
        the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        parameter : str or list[str]
                    a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : datetime.date
                a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : datetime.date
                a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        MA_code : str
                  a python character object which represents the 4 digit AQS
                  Monitoring Agency code (with leading zeroes).
        service : str
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        cbdate : datetime.date, optional
                 a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : datetime.date, optional
                 a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        '''
    def _aqs_list_services(self, aqsfilter: str, countycode: str | None = None, stateFIPS: str | None = None, cbsa_code: str | None = None, MA_code: str | None = None, pqao_code: str | None = None, parameterclass: str | None = None) -> DataFrame | None:
        """Call _aqs for functions using the list service.

        This is a helper method and should not be called by the end user. This method is used by list functions to call
        the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        aqsfilter : str or list[str]
                    a string which represents the filter used in conjunction
                    with the service requested. For a list of available
                    services and filters see
                    https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        countycode : str, optional
                     a python character object which represents the 3 digit
                    state FIPS code for the county being requested
                    (with leading zero(s)). Use aqs_counties_by_state() for
                    the list of available county codes for each state.
        stateFIPS : str, optional
                    a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        cbsa_code : str, optional
                   a python character object which represents the 5 digit AQS
                   Core Based Statistical Area code (the same as the census
                   code, with leading zeros).
        MA_code : str, optional
                  a python character object which represents the 4 digit AQS
                  Monitoring Agency code (with leading zeroes).
        pqao_code : str, optional
                    a python character object which represents the 4 digit AQS
                    Primary Quality Assurance Organization code
                    (with leading zeroes).
        parameterclass: str, optional
                    a python character object that represents the class
                    requested, use aqs_classes() for retrieving available
                    classes. The parameterclass python character object must be
                    a valid parameterclass as returned from aqs_classes().
                    The class must be an exact match to what is returned from
                    aqs_classes().

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        """
    def _aqs_metadata_services(self, aqsfilter: str | None = None, service: str | None = None) -> DataFrame | None:
        """Call _aqs for functions using the metadata service.

        This is a helper method and should not be called by the end user. This method is used by list functions to call
        the AQSAPI_V2._aqs() method.

        Parameters
        ----------
        aqsfilter : str, optional
                    a string which represents the filter used in conjunction
                    with the service requested. For a list of available
                    services and filters see
                    https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        service : str, optional
                  the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        """
    def _renameaqsvariables(self, name1: str, name2: str) -> DataFrame:
        '''Rename Data columns in the data portion of a AQSAPI_v2 object.

        The data columns are renamed from "value" and "value_represented" to name1 and name2 respectively.

        This is a helper method, not intended to be called directly
        by the end user.

        Parameters
        ----------
        name1 : str
            a character string representing the new name of the first column of
            the Data portion of the AQSAPI_V2 object. (can be set to None)
        name2 : str
           a character string representing the new name of the second
           column of the Data portion of the AQSAPI_V2 object. (can be set to
           None)

        Returns
        -------
        (AQSAPI_V2) the input DataFrame with data columns renamed
        to name1 and name2 respectively.

        '''

def aqs_credentials(username: str | None = None, key: str | None = None) -> None:
    """Set the user credentials for the AQS API.

    This function needs to be called once and only once every time this library
    is re-loaded. Users must have a valid username and key which
    can be obtained through the use of the aqs_sign_up function,
    use pyaqsapi.aqs_sign_up() to sign up for AQS data mart credentials.

    Parameters
    ----------
    username : str
               a python character object which represents the email account
               that will be used to connect to the AQS API.
    key : str
          the key used in conjunction with the username given to connect to
          AQS Data Mart.

    Returns
    -------
    None

    """
def aqs_removeheader(aqsobject: None | DataFrame | AQSAPI_V2 | list[DataFrame] | list[AQSAPI_V2]) -> DataFrame | AQSAPI_V2:
    """Coerces a single AQS_Data_Mart_APIv2 instance or a list of AQS_Data_Mart_APIv2 instance into a single DataFrame.

    This function decouples the Data from the AQSAPI_v2 object and returns
    only the Data portion as a DataFrame. If the input is a list of AQSAPI_v2
    objects this function combines the Data portion of each AQS_Data_Mart_APIv2 object
    into a DataFrame with Header information discarded, else returns the input with no changes.

    Parameters
    ----------
    aqsobject : pyaqsapi.helperfunctions.AQSAPI_V2
        An object of AQSAPI_v2 or a list of AQSAPI_v2 objects.

    Returns
    -------
    (DataFrame) A DataFrame containing the data portion of the AQSAPI_V2
    object.

    """
def _aqsmultiyearcall(fun: str, parameter: str, bdate: date, edate: date, service: str, singlecall: bool | None = False, **kwargs: Any) -> list[DataFrame] | None:
    """Make multiple calls to _aqs.

       This is a helper function, not to be used by end users. Used to perform multiple calls to the API on API calls which
       only allow a single year of data to be returned, simplifying multi-year calls for the end user.

       This function is used to make multiple calls to the Datamart API for request for data that exceed the request limit
       set by AQS Datamart. This is done by making multiple API request to the API and combining the results from all
       requests into a single manageable object that is returned to the calling function for further processing. The first
       seven parameters (fun, parameter, bdate, edate, service, name1 and name2) are all required parameters that must be
       including in the function call (Name1 and Name2 can be set to None). Other parameters are captured by **kwargs to
       be sent to the API. These optional parameters include sitenum, countycode, stateFIPS, cbsa_code, ma_code, minlat,
       maxlat, minlon, pqao_code, duration, cbdate and cedate for API calls that require those parameters.


    Creates a DataFrame
        containing all variables to be passed to multiyearcall()) with each
        column representing a singe parameter and each row a single call
        to the API.

    Parameters
    ----------
    fun : str
        The name of the pyaqsapi.services_by_* helperfunction to be called
        represented as a string.
    parameter : str or list[str]
        a character list or a single character string
        which represents the parameter code of the air
        pollutant related to the data being requested.
    bdate : datetime.date
        a python date object which represents that begin date of the
        data selection. Only data on or after this date will be
        returned.
    edate : datetime.date
        a python date object which represents that end date of the data
        selection. Only data on or before this date will be returned.
    service : str
        the service requested by the AQS API encoded as a string;
        For a list of available services see
        https://aqs.epa.gov/aqsweb/documents/data_api.html#services
    singlecall : bool, optional
        Default: False. A boolean value, when set to True will send multiple
        years of data as a single API call. Currently only the monitors
        service supports this functionality.
    **kwargs : optional
        additional parameters to be set to the API as needed for each
        API service requested. These optional parameters include
        sitenum, countycode, stateFIPS, cbsa_code, ma_code, minlat,
        maxlat, minlon, pqao_code, duration, cbdate and cedate.
        Refer to the the _services_by_ functions documentation for
        details on those additional parameters.

    Warns
    -----
    UserWarning
    A UserWarning is thrown if bdate > edate, a  NameError is thrown if fun is not one of the available
    AQSAPI_V2 service helper functions.

    Returns
    -------
    (list of itertools starmap objects): A list of itertools.starmap objects
    that contain AQSAPI_V2 objects where each item in the list represents a
    single call to the AQS Datamart API. The aqs_removeheader function can
    be used to simplify the returned list into a single DataFrame.

    """
