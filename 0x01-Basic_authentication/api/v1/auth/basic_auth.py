#!/usr/bin/env python3
"""
BasicAuth class module
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentification class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extracts the Base64 part of the Authorization header """
        if (not authorization_header
                or not isinstance(authorization_header, str)
                or not authorization_header.startswith("Basic ")):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64 string """
        if (not base64_authorization_header
                or not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
        except base64.binascii.Error as e:
            return None

        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
