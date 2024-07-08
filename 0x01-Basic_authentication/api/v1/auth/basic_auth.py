#!/usr/bin/env python3
"""
BasicAuth class module
"""
from api.v1.auth.auth import Auth


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
