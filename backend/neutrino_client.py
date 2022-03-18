import requests
from neutrino_api.neutrino_api_client import NeutrinoApiClient
from neutrino_api.controllers.security_and_networking import SecurityAndNetworking
import os


class NeutrinoClient:

    @staticmethod
    def connect():
        user_id = "amit_az3354"
        api_key = "1FANb7Rwh3rVzN0VJewvpyYDXUbgo2RUVEuG7Bmnxi1mIsfr"
        return NeutrinoApiClient(user_id, api_key)
