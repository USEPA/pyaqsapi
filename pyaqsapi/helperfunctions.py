# -*- coding: utf-8 -*-
"""helperfunctions."""

from datetime import date
from itertools import starmap
from time import sleep
from warnings import warn

from certifi import where
from pandas import DataFrame, concat
from requests import get

AQS_user = None
AQS_key = None


class AQSAPI_V2:
    """
     AQSAPI_V2 class used to store and retrieve data from the EPA AQS
     Datamart API.

      # for some reason Sphinx does not like this Attributes section so it is
      # commented out, for now.

      # Attributes
      # ----------
      # _header (pandas DataFrame): header information returned from the
      #     AQS Datamart API.
      # _request_time (str): the time stamp that the call to the AQS Datamart
      #     API was received.
      # _status (str): the status (associated with the _status_code) returned
      #     from a call to the AQS Datamart API.
      # _status_code (str): the numeric status_code (represented as a string)
      #     that is returned from a call to the AQS Datamart API.
      # _rows (str): the number of rows contained in the _data.
      # _url (str): a string representing the URL used to make the AQS Datamart
      #     API call.
      # _data (pandas DataFrame): the data returned from a call to the
      #     AQS Datamart API.

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

    """

    def __init__(self):
        """Initiate the AQSAPI_V2 instance."""
        self._header = DataFrame()
        self._data = DataFrame()
        self._request_time = None
        self._rows = None
        self._url = None
        self._request_time = None

    def set_header(self, Header):
        """
        Set the header of a single AQSAPI_V2 object. Header must be a
        pandas DataFrame.

        Warns
        -----
        A warning is thrown if Header is not a pandas DataFrame

        Parameters
        ----------
        Header : Pandas DataFrame
            A pandas.DataFrame instance with the header information.

        Returns
        -------
        None.

        """
        if isinstance(Header, DataFrame):
            self._header = Header
        else:
            warn("AQSAPI_V2 header must be a pandas DataFrame", UserWarning)

    def get_data(self):
        """
        Return the Data portion of the AQSAPI_V2 instance.

        Returns
        -------
        (pandas DataFrame) a DataFrame containing the Data portion of the
        AQSAPI_V2 instance.

        """
        return self._data

    def set_data(self, Data):
        """
        Set the Data of a single AQSAPI_V2 object.

        Data must be a pandas DataFrame.

        Warns
        -----
        A warning is thrown if Data is not a pandas DataFrame

        """
        if isinstance(Data, DataFrame):
            self._data = Data
        else:
            warn("AQSAPI_V2 data must be a pandas DataFrame", UserWarning)

    def get_header(self):
        """
        Return the Header portion of the AQSAPI_V2 instance.

        Returns
        -------
        (pandas DataFrame) a DataFrame containing the Header portion of the
        AQSAPI_V2 instance.

        """
        return self._header

    def get_status_code(self):
        """
        Retrieve the status code from the API call.

        Returns
        -------
        (str) A string representing the status code returned from the EPA
        DataMart API.

        """
        return self._status_code

    def get_url(self):
        """
        Retrieve the URL of the AQS DataMart API request.

        Returns
        -------
        (str) A string representing the status code returned from the EPA
        DataMart API.

        """
        return self._url

    def _set_status_code(self, status_code):
        """
        Set the status code of the AQS DataMart API call.

        Parameter
        ---------
        status_code : A string representing the status code

        Returns
        -------
        None

        """
        self.status_code = status_code

    def get_request_time(self):
        """
        Retrieve the time that the request to the AQS DataMart API was made.

        Returns
        -------
        (str) A string representing the time that that request to the AQS
        DataMart API was made.

        """
        return self._request_time

    def __aqs_ratelimit(self, waittime=5):
        """
        A wrapper function to time.sleep() used as a rudimentary ratelimit
        between API requests.

        This is a helper function not intended for end use.

        Parameters
        ----------
        waittime : int
            An integer representing the amount of time in seconds that the
            function should wait before executing the next API call.

        Note
        ----
        Although this function is designed to prevent users from exceeding
        allowed data limits, it can not garuntee that the user exceed rate
        limits. Users are advised to monitor their own usage to ensure that
        data limits are not exceeded. Use of this package is at the users own
        risk. The maintainers of this code assume no responsibility due to
        anything that may happen as a result of using this code.

        Returns
        -------
        None.

        """
        sleep(waittime)

    def __aqs(
        self,
        service=None,
        aqsfilter=None,
        variables=None,
        AQS_user=None,
        key=None,
        AQS_domain="https://aqs.epa.gov/data/api/",
    ):
        """
        Sends  AQS request to the AQS API and returns the result.

        This helper function is used to abstract the call to AQS API away from
        functions that need it's result. This helper function is not
        meant to be called directly from external functions.

        Parameters
        ----------
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        filter : a string which represents the filter used in conjunction with
                 the service requested. For a list of available services
                 and filters see
                 https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        variables : A python dictionary of containing key-value pairs of
                    variables to be sent to the AQS DataMart API.
        AQS_user : A python character object which represents the email account
                   that will be used to autheticate with the AQS API.
        key : The key associated with the AQS_user account represented as a
              character string.
        AQS_domain : The base domain for the url used in API requests. Normally
                     this should be set to <https://aqs.epa.gov/data/api/>,
                     this parameter allows the domain to be overridden.

        Returns
        -------
        (AQSAPI_v2) An AQSAPI_V2 instance containg the data requested.

        """
        user_agent = "pyAQSAPI module for python3"
        # server = ":AQSDatamartAPI:"
        # check if either aqs_username or aqs_key are None
        if AQS_user is None or key is None:
            print(
                "Please use the aqs_credentials  function to enter your",
                "credentials before using this function",
            )
            return ()
        # key is formatted like this to maintain consitency with RAQSAPI
        # key = keyring.get_password(service_name = server +
        # re.sub(pattern = "@", repl = "%40", string = AQS_user),
        # username = AQS_user )
        # rename the "parameter" key to "param" if it exists.
        if "parameter" in variables.keys():
            variables["param"] = variables.pop("parameter")
        if "stateFIPS" in variables.keys():
            variables["state"] = variables.pop("stateFIPS")
        if "class" in variables.keys():
            variables["pc"] = variables.pop("class")
        if "county_code" in variables.keys():
            variables["county"] = variables.pop("county_code")
        if "edate" in variables.keys() and variables["edate"] is not None:
            variables["edate"] = variables["edate"].strftime(format="%Y%m%d")
        if "bdate" in variables.keys() and variables["bdate"] is not None:
            variables["bdate"] = variables["bdate"].strftime(format="%Y%m%d")
        if "cedate" in variables.keys() and variables["cedate"] is not None:
            variables["cedate"] = variables["cedate"].strftime(format="%Y%m%d")
        if "cbdate" in variables.keys() and variables["cbdate"] is not None:
            variables["cbdate"] = variables["cbdate"].strftime(format="%Y%m%d")
        if service is None:
            service = ""
        url = AQS_domain + service + "/" + aqsfilter
        # AQS_domain = "https://aqs.epa.gov/data/api/" + service + "/" + aqsfilter
        header = {"User-Agent": user_agent, "From": AQS_user}

        query = get(url=url, params=variables, headers=header, verify=where())
        query.raise_for_status()
        self.set_header(DataFrame(query.headers))
        self.set_data(DataFrame.from_dict(query.json()["Data"]))
        self._url = query.url
        self._status_code = query.status_code
        self.__aqs_ratelimit()
        return self

    def _aqs_services_by_site(
        self,
        parameter,
        bdate,
        edate,
        stateFIPS,
        countycode,
        sitenum,
        service,
        duration=None,
        cbdate=None,
        cedate=None,
    ):
        """
        This is a helper function and should not be called by the end user.

        This function is used by bysite functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        stateFIPS : a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        countycode : a python character object which represents the 3 digit
                    state FIPS code for the county being requested
                    (with leading zero(s)). Use aqs_counties_by_state() for
                    the list of available county codes for each state.
        sitenum : a python character object which represents the 4 digit site
                  number (with leading zeros) within the county and state
                  being requested.
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        """
        global AQS_user
        global AQS_key
        user = AQS_user
        key = AQS_key
        aqsfilter = "bySite"
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "state": stateFIPS,
            "county": countycode,
            "site": sitenum,
            "duration": duration,
            "cedate": cedate,
            "cbdate": cbdate,
        }
        return self.__aqs(
            AQS_user=user,
            key=key,
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
        )

    def _aqs_services_by_county(
        self,
        parameter,
        bdate,
        edate,
        stateFIPS,
        countycode,
        service,
        duration=None,
        cbdate=None,
        cedate=None,
    ):
        """
        This is a helper function and should not be called by the end user.

        This function is used by bycounty functions to call the
        AQSAPI_V2._aqs() function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        stateFIPS : a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        countycode : a python character object which represents the 3 digit
                    state FIPS code for the county being requested
                    (with leading zero(s)). Use aqs_counties_by_state() for
                    the list of available county codes for each state.
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        """
        global AQS_user
        global AQS_key
        aqsfilter = "byCounty"
        user = AQS_user
        key = AQS_key
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "state": stateFIPS,
            "county": countycode,
            "duration": duration,
            "cbdate": cbdate,
            "cedate": cedate,
        }
        return self.__aqs(
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
            AQS_user=user,
            key=key,
        )

    def _aqs_services_by_state(
        self,
        parameter,
        bdate,
        edate,
        stateFIPS,
        service,
        duration=None,
        cbdate=None,
        cedate=None,
    ):
        """
        A helper function and should not be called by the end user.
        This function is used by bystate functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        stateFIPS : a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.

        """
        global AQS_user
        global AQS_key
        aqsfilter = "byState"
        user = AQS_user
        key = AQS_key
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "state": stateFIPS,
            "duration": duration,
            "cbdate": cbdate,
            "cedate": cedate,
        }
        return self.__aqs(
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
            AQS_user=user,
            key=key,
        )

    def _aqs_services_by_box(
        self,
        parameter,
        bdate,
        edate,
        minlat,
        maxlat,
        minlon,
        maxlon,
        service,
        duration=None,
        cbdate=None,
        cedate=None,
    ):
        """
        A helper function and should not be called by the end user.
        This function is used by bybox functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        minlat : a python character object which represents the minimum
                 latitude of a geographic box. Decimal latitude with north
                 begin positive. Only data north of this latitude will be
                 returned.
        maxlat : a python character object which represents the maximum
                 latitude of a geographic box. Decimal latitude with north
                 begin positive. Only data south of this latitude will be
                 returned.
        minlon : a python character object which represents the minimum
                 longitude of a geographic box. Decimal longitude with east
                 begin positive. Only data east of this longitude will be
                 returned.
        maxlon : a python character object which represents the maximum
                 longitude of a geographic box. Decimal longitude with east
                 begin positive. Only data west of this longitude will be
                 returned. Note that -80 is less than -70.
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        """
        global AQS_user
        global AQS_key
        aqsfilter = "byBox"
        user = AQS_user
        key = AQS_key
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "minlat": minlat,
            "maxlat": maxlat,
            "minlon": minlon,
            "maxlon": maxlon,
            "duration": duration,
            "cbdate": cbdate,
            "cedate": cedate,
        }
        return self.__aqs(
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
            AQS_user=user,
            key=key,
        )

    def _aqs_services_by_cbsa(
        self,
        parameter,
        bdate,
        edate,
        cbsa_code,
        service,
        duration=None,
        cbdate=None,
        cedate=None,
    ):
        """
        A helper function and should not be called by the end user.
        This function is used by bycbsa functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        cbsa_code: a python character object which represents the 5 digit AQS
                   Core Based Statistical Area code (the same as the census
                   code, with leading zeros).
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        """
        global AQS_user
        global AQS_key
        aqsfilter = "byCBSA"
        user = AQS_user
        key = AQS_key
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "cbsa": cbsa_code,
            "duration": duration,
            "cbdate": cbdate,
            "cedate": cedate,
        }
        return self.__aqs(
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
            AQS_user=user,
            key=key,
        )

    def _aqs_services_by_pqao(
        self,
        parameter,
        bdate,
        edate,
        pqao_code,
        service,
        cbdate=None,
        cedate=None,
    ):
        """
        A helper function and should not be called by the end user.
        This function is used by bypqao functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        pqao_code : a python character object which represents the 4 digit AQS
                    Primary Quality Assurance Organization code
                    (with leading zeroes).
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        duration : an optional python character string that represents the
                   parameter duration code that limits returned data to a
                   specific sample duration. The default value of None results
                   in no filtering based on duration code.Valid durations
                   include actual sample durations and not calculated durations
                   such as 8 hour carbon monoxide or ozone rolling averages,
                   3/6 day PM averages or lead 3 month rolling averages. Use
                   aqs_sampledurations() for a list of all available
                   duration codes.
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.
        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        """
        global AQS_user
        global AQS_key
        aqsfilter = "byPQAO"
        user = AQS_user
        key = AQS_key
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "pqao": pqao_code,
            "cbdate": cbdate,
            "cedate": cedate,
        }
        return self.__aqs(
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
            AQS_user=user,
            key=AQS_key,
        )

    def _aqs_services_by_MA(
        self,
        parameter,
        bdate,
        edate,
        MA_code,
        service,
        cbdate=None,
        cedate=None,
    ):
        """
        A helper function and should not be called by the end user.
        This function is used by byma functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        MA_code : a python character object which represents the 4 digit AQS
                  Monitoring Agency code (with leading zeroes).
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        cbdate : a python date object which represents a "beginning date of
                 last change" that indicates when the data was last updated.
                 cbdate is used to filter data based on the change date.
                 Only data that changed on or after this date will be
                 returned. This is an optional variable which defaults to
                 None.
        cedate : a python date object which represents an "end date of last
                 change" that indicates when the data was last updated.
                 cedate is used to filter data based on the change date.
                 Only data that changed on or before this date will be
                 returned. This is an optional variable which defaults
                 to None.

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        """
        global AQS_user
        global AQS_key
        aqsfilter = "byMA"
        user = AQS_user
        key = AQS_key
        variables = {
            "email": user,
            "key": key,
            "param": parameter,
            "bdate": bdate,
            "edate": edate,
            "agency": MA_code,
            "cbdate": cbdate,
            "cedate": cedate,
        }
        return self.__aqs(
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
            AQS_user=user,
            key=AQS_key,
        )

    def _aqs_list_services(
        self,
        aqsfilter,
        countycode=None,
        stateFIPS=None,
        cbsa_code=None,
        MA_code=None,
        pqao_code=None,
        parameterclass=None,
    ):
        """
        A helper function and should not be called by the end user.
        This function is used by list functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        aqsfilter : a string which represents the filter used in conjunction
                    with the service requested. For a list of available
                    services and filters see
                    https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        countycode : a python character object which represents the 3 digit
                    state FIPS code for the county being requested
                    (with leading zero(s)). Use aqs_counties_by_state() for
                    the list of available county codes for each state.
        stateFIPS : a python character object which represents the 2 digit
                    state FIPS code (with leading zero) for the state being
                    requested. Use aqs_states() for the list of available
                    FIPS codes.
        cbsa_code : a python character object which represents the 5 digit AQS
                   Core Based Statistical Area code (the same as the census
                   code, with leading zeros).
        MA_code : a python character object which represents the 4 digit AQS
                  Monitoring Agency code (with leading zeroes).
        pqao_code : a python character object which represents the 4 digit AQS
                    Primary Quality Assurance Organization code
                    (with leading zeroes).
        parameterclass: a python character object that represents the class
                    requested, use aqs_classes() for retrieving available
                    classes. The parameterclass python character object must be
                    a valid parameterclass as returned from aqs_classes().
                    The class must be an exact match to what is returned from
                    aqs_classes().

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        """
        global AQS_user
        global AQS_key
        user = AQS_user
        key = AQS_key
        service = "list"
        variables = {
            "email": AQS_user,
            "key": AQS_key,
            "county_code": countycode,
            "stateFIPS": stateFIPS,
            "cbsa_code": cbsa_code,
            "class": parameterclass,
            "pqao_code": pqao_code,
            "agency": MA_code,
        }
        return self.__aqs(
            AQS_user=user,
            key=key,
            service=service,
            aqsfilter=aqsfilter,
            variables=variables,
        )

    def _aqs_metadata_services(self, aqsfilter=None, service=None):
        """
        A helper function and should not be called by the end user.
        This function is used by list functions to call the AQSAPI_V2._aqs()
        function.

        Parameters
        ----------
        aqsfilter : a string which represents the filter used in conjunction
                    with the service requested. For a list of available
                    services and filters see
                    https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services

        Returns
        -------
        (pandas DataFrame or an AQSAPI_V2 object): The information requested.
        """
        global AQS_user
        global AQS_key
        user = AQS_user
        key = AQS_key
        variables = {"email": user, "key": key, "service": service}
        return self.__aqs(
            AQS_user=user,
            key=key,
            service="metaData",
            aqsfilter=aqsfilter,
            variables=variables,
        )

    def _renameaqsvariables(self, name1, name2):
        """
        This is a helper function not intended to be called directly
        by the end user. Renames the two columns returned in the Data
        portion of a AQSAPI_v2 object from "value" and
        "value_represented" to name1 and name2 respectively.

        Parameters
        ----------
        self : an AQSAPI_V2 object
            DESCRIPTION.
        name1 : str
            a character string representing the new name of the first column of
            the Data portion of the AQSAPI_V2 object. (can be set to None)
        name2 : str
           a character string representing the new name of the second
           column of the Data portion of the AQSAPI_V2 object. (can be set to
           None)

        Returns
        -------
        (aqsobject) the input DataFrame with data columns renamed
        to name1 and name2 respectively.

        """
        self._data.rename(
            columns={
                self._data.columns[0]: name1,
                self._data.columns[1]: name2,
            },
            inplace=True,
        )


def aqs_credentials(username=None, key=None):
    """
    Sets the user credentials for the AQS API. This function
    needs to be called once and only once every time this library
    is re-loaded. Users must have a valid username and key which
    can be obtained through the use of the aqs_sign_up function,
    use pyaqsapi.aqs_sign_up() to sign up for AQS data mart credentials.

    Parameters
    ----------
    username : a python character object which represents the email account
                   that will be used to connect to the AQS API.
    key : the key used in conjunction with the username given to connect to
              AQS Data Mart.

    Returns
    -------
    None

    """
    if not (username is None or key is None):
        global AQS_user
        global AQS_key
        AQS_user = username
        AQS_key = key
    else:
        print("username: ", username)
        print("key: ", key)
        print(f"AQS_user, {AQS_user}", AQS_user)
        print(f"AQS_key {AQS_key}", AQS_key)
        print("Please set the username and key parameters")


def aqs_removeheader(aqsobject):
    """
    Coerces a single AQS_Data_Mart_APIv2 instance or a list of
    AQS_Data_Mart_APIv2 instance into a single DataFrame object.
    This function decouples the Data from the AQSAPI_v2 object and returns
    only the Data portion as a DataFrame. If the input is a list of AQSAPI_v2
    objects combines the Data portion of each AQS_Data_Mart_APIv2 object
    into a DataFrame with Header information discarded.
    Else returns the input with no changes.

    Parameters
    ----------
    aqsobject : An object of AQSAPI_v2 or a list of AQSAPI_v2 objects.

    Returns
    -------
    (DataFrame) A DataFrame containing the data portion of the AQSAPI_V2
    object.

    """
    aqsresult = DataFrame()
    for x in range(len(aqsobject)):
        aqsresult = concat([aqsresult, aqsobject[x].get_data()], axis=0)

    return aqsresult


def _aqsmultiyearcall(fun, parameter, bdate, edate, service, name1, name2, **kwargs):
    """
        A helper function not to be used by end users.

        This function is used to make multiple calls to the Datamart API for
        request for data that exceed the request limit set by AQS Datamart.
        This is done by making multiple API request to the API and combining the
        results from all requests into a single managable object that is returned
        to the calling function for further processing. The first seven parameters
        (fun, parameter, bdate, edate, service, name1 and name2) are all required
        parameters that must be including in the function call (Name1 and Name2
        can be set to None). Other parameters are captured by **kwargs to be sent
        to the API. These optional parameters include sitenum, countycode,
        stateFIPS, cbsa_code, ma_code, minlat, maxlat, minlon, pqao_code, duration,
        cbdate and cedate for API calls that require those parameters.


    Creates a DataFrame
        containing all vaiables to be passed to multiyearcall()) with each column
        representing a singe parameter and each row a single call to the API.

        Parameters
        ----------
        fun : The name of the pyaqsapi.services_by_* helperfunction to be called
              represented as a string.
        parameter : a character list or a single character string
                    which represents the parameter code of the air
                    pollutant related to the data being requested.
        bdate : a python date object which represents that begin date of the
                data selection. Only data on or after this date will be
                returned.
        edate : a python date object which represents that end date of the data
                selection. Only data on or before this date will be returned.
        service : the service requested by the AQS API encoded as a string;
                  For a list of available services see
                  https://aqs.epa.gov/aqsweb/documents/data_api.html#services
        name1 : str
                a character string representing the new name of the first column of
                the Data portion of the AQSAPI_V2 object. (can be set to None)
        name2 : str
                a character string representing the new name of the second
                column of the Data portion of the AQSAPI_V2 object. (can be set to
                None)
        **kwargs : additional parameters to be set to the API as needed for each
                   API service requested. These optional parameters include
                   sitenum, countycode, stateFIPS, cbsa_code, ma_code, minlat,
                   maxlat, minlon, pqao_code, duration, cbdate and cedate.
                   Refer to the the _services_by_ functions documentation for
                   details on those additional parameters.

        Warns
        -----
        A warning is thrown if bdate > edate

        Returns
        -------
        (list of itertools starmap objects): A list of itertools.starmap objects
        that contain AQSAPI_V2 objects where each item in the list represents a
        single call to the AQS Datamart API. The aqs_removeheader function can be
        used to simplify the returned list into a single DataFrame.

    """
    aqsresult = AQSAPI_V2()  # ignore the variable not used warning.
    if bdate > edate:
        # throw a warning if bdate > edate
        warn("bdate > edate", UserWarning)
    elif bdate.year == edate.year:
        # create date lists of a single year
        edatelist = [edate]
        bdatelist = [bdate]
    elif bdate.year < edate.year:
        # if bdate < edate and not a single year then generate a list of
        # begin dates and end dates with the list of begin dates starting with
        # bdate followed by January 1 for each year until end date (including
        # the year of bdate and not that of edate)
        # likewise, the list of end dates should be December 31 for each year
        # until end date (including the year of bdate and not the year of
        # edate) with edate appended to the end.
        bdatelist = [
            date(year=x, month=1, day=1) for x in range(bdate.year + 1, edate.year + 1)
        ]
        bdatelist.insert(0, bdate)
        edatelist = [
            date(year=y, month=12, day=31) for y in range(bdate.year, edate.year)
        ]
        edatelist.append(edate)

    params = DataFrame(
        {
            "parameter": parameter,
            "bdate": bdatelist,
            "edate": edatelist,
            "service": service,
        }
    )

    for k, v in kwargs.items():
        params.insert(0, k, v)

    params = params.reindex(
        columns=[
            "parameter",
            "bdate",
            "edate",
            "stateFIPS",
            "countycode",
            "sitenum",
            "MA_code",
            "pqao_code",
            "cbsa_code",
            "minlat",
            "maxlat",
            "minlon",
            "maxlon",
            "service",
            "duration",
            "cbdate",
            "cedate",
        ]
    )
    params = params.dropna(axis="columns", how="any")
    params = [tuple(x) for x in params.values]
    # match fun: #requires Python>=3.10, use if statements instead
    #     case "_aqs_services_by_site":
    #         return(list(starmap(aqsresult._aqs_services_by_site, params)))
    #     case "_aqs_services_by_county":
    #         return(list(starmap(aqsresult._aqs_services_by_county, params)))
    #     case "_aqs_services_by_state":
    #         return(list(starmap(aqsresult._aqs_services_by_state, params)))
    #     case "_aqs_services_by_MA":
    #         return(list(starmap(aqsresult._aqs_services_by_MA, params)))
    #     case "_aqs_services_by_pqao":
    #         return(list(starmap(aqsresult._aqs_services_by_pqao, params)))
    #     case "_aqs_services_by_cbsa":
    #         return(list(starmap(aqsresult._aqs_services_by_cbsa, params)))
    #     case "_aqs_services_by_box":
    #         return(list(starmap(aqsresult._aqs_services_by_box, params)))
    #     case _:
    #         RuntimeError("invalid function sent to _aqsmultiyearcall")
    if fun == "_aqs_services_by_site":
        return list(starmap(aqsresult._aqs_services_by_site, params))
    elif fun == "_aqs_services_by_county":
        return list(starmap(aqsresult._aqs_services_by_county, params))
    elif fun == "_aqs_services_by_state":
        return list(starmap(aqsresult._aqs_services_by_state, params))
    elif fun == "_aqs_services_by_MA":
        return list(starmap(aqsresult._aqs_services_by_MA, params))
    elif fun == "_aqs_services_by_pqao":
        return list(starmap(aqsresult._aqs_services_by_pqao, params))
    elif fun == "_aqs_services_by_cbsa":
        return list(starmap(aqsresult._aqs_services_by_cbsa, params))
    elif fun == "_aqs_services_by_box":
        return list(starmap(aqsresult._aqs_services_by_box, params))
