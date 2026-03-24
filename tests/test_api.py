# BUILT-IN
import unittest
from os import getenv

# EXTERNAL
from requests import HTTPError

# INTERNAL
from pysignalclirestapi import SignalCliRestApi
from pysignalclirestapi import SignalCliRestApiHTTPBasicAuth

# CODE

# TO USE THESE TESTS, YOU MUST HAVE AN ACTUAL API INSTANCE AVAILABLE

class TestInitializingBasic(unittest.TestCase):
    """
    Test the class initialization
    """
    def test_no_args(self):
        """
        Ensure initialization fails if no arguments are passed
        """
        with self.assertRaises(TypeError):
            client = SignalCliRestApi()
    
    #TODO complete the basics here
    
class TestInitializingNoAuth(unittest.TestCase):
    """
    Test the class initialization where API doesn't have any authentication
    
    THESE TESTS ARE ONLY INTENDED FOR API INSTANCES WITH NO AUTHENTICATION!
    """
    
    def test_auth_not_configured(self):
        """
        Ensure initialization fails if authentication arguments are passed when no authentication is required
        """
        pass
    
    #TODO complete
        
class TestInitializingBasicAuth(unittest.TestCase):
    """
    Test the class initialization where API has basic authentication
    
    THESE TESTS ARE ONLY INTENDED FOR API INSTANCES WITH BASIC HTTP AUTHENTICATION!
    
    ENSURE YOU HAVE THE FOLLOWING ENVIRONMENT VARIABLES:
        NUMBER: The Signal account number
        BASIC_AUTH_API_URL: URL for your Signal API instance (WITH BASIC AUTH)
        BASIC_AUTH_USER: Basic auth username
        BASIC_AUTH_PASS: Basic auth password
    """
    def setUp(self):
        self._NUMBER: str = getenv("NUMBER", None)
        self._BASIC_AUTH_API_URL:str = getenv("BASIC_AUTH_API_URL", None)
        self._BASIC_AUTH_USER:str = getenv("BASIC_AUTH_USER", None)
        self._BASIC_AUTH_PASS:str = getenv("BASIC_AUTH_PASS", None)
    
    def test_environment_variables_present(self):
        """
        Ensure the required environment variables have been provided
        """
        self.assertIsNotNone(self._NUMBER, msg="Missing number")
        self.assertIsNotNone(self._BASIC_AUTH_API_URL, msg="Missing API url for basic auth")
        self.assertIsNotNone(self._BASIC_AUTH_USER, msg="Missing basic auth user")
        self.assertIsNotNone(self._BASIC_AUTH_PASS, msg="Missing basic auth password")
        
    def test_auth_valid(self):
        """
        Ensure initialization succeeds with basic auth
        """
        auth = SignalCliRestApiHTTPBasicAuth(
            basic_auth_user=self._BASIC_AUTH_USER,
            basic_auth_pwd=self._BASIC_AUTH_PASS
            )
        client = SignalCliRestApi(
            base_url=self._BASIC_AUTH_API_URL,
            number=self._NUMBER,
            auth=auth
        )
        
    def test_auth_not_provided(self):
        """
        Ensure initialization fails if the API reuires authentication and the 'auth' argument isn't passed
        """
        with self.assertRaises(HTTPError, msg=""):
            client = SignalCliRestApi(
                base_url=self._BASIC_AUTH_API_URL,
            )
    
    #TODO complete
        
    
class TestGroupMethods(unittest.TestCase):
    def setUp(self):
        client = SignalCliRestApi(
            base_url="",
            number=""
        )
        
