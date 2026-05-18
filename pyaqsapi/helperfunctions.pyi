from pandas import DataFrame

AQS_user: str | None
AQS_key: str | None
ONE_MINUTE: int

class AQSAPI_V2:
    """AQSAPI_V2 class used to store and retrieve data from the EPA AQS
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
    get_status()
    get_numberofrows()
    """

    def __init__(self) -> None:
        """Initiate the AQSAPI_V2 instance."""

    def set_header(self, Header: DataFrame) -> None:
        """Set the header of a single AQSAPI_V2 object. Header must be a
        pandas DataFrame.

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
        """Retrieve the number of rows of data returned from the API call. This information can be used to track the amount
        of data requested.

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

def aqs_credentials(username: str | None = None, key: str | None = None) -> None:
    """Set the user credentials for the AQS API. This function
    needs to be called once and only once every time this library
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
    """Coerces a single AQS_Data_Mart_APIv2 instance or a list of
    AQS_Data_Mart_APIv2 instance into a single DataFrame object.
    This function decouples the Data from the AQSAPI_v2 object and returns
    only the Data portion as a DataFrame. If the input is a list of AQSAPI_v2
    objects combines the Data portion of each AQS_Data_Mart_APIv2 object
    into a DataFrame with Header information discarded,
    else returns the input with no changes.

    Parameters
    ----------
    aqsobject : pyaqsapi.helperfunctions.AQSAPI_V2
        An object of AQSAPI_v2 or a list of AQSAPI_v2 objects.

    Returns
    -------
    (DataFrame) A DataFrame containing the data portion of the AQSAPI_V2
    object.

    """
