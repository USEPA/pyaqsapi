"""setupfunctions."""

from requests import get


def aqs_sign_up(email):  # pragma: no cover
    """
    Use this service to register as a new user or to reset an existing user's
    key. A verification email will be sent to the email account specified. To
    reset a password: If the request is made with an email that is already
    registered, a new key will be issued for that account and emailed to the
    listed address. Usage is the same in either case. Refer to the email
    message for further instructions before continuing.

    Parameters
    ----------
    email : A python character object which represents the email account that
            will be used to register with the AQS API or change an existing
            user's key. A verification email will be sent to the account
            specified. Follow the instructions in the verification e-mail
            before proceeding to use any other functionality of the AQS API.
            Register your credential with the aqs_credentials() before using
            the other functions in this library.


    Returns
    -------
    None.
    """
    url = "https://aqs.epa.gov/data/api/signup?email=" + email
    print(f"A verification email will be sent to {email}", email)
    get(url=url)
