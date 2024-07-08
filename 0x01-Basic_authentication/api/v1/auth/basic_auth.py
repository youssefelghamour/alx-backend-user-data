#!/usr/bin/env python3
"""
BasicAuth class module
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Returns the user email and password from the decoded Base64 str """
        if (not decoded_base64_authorization_header
                or not isinstance(decoded_base64_authorization_header, str)
                or ":" not in decoded_base64_authorization_header):
            return (None, None)

        email = decoded_base64_authorization_header.split(":")[0]
        password = decoded_base64_authorization_header.split(":")[1]

        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password """
        if (not user_email or not isinstance(user_email, str)
                or not user_pwd or not isinstance(user_pwd, str)):
            return None

        # returns a list of user
        users = User.search({'email': user_email})
        if len(users) > 0:
            if users[0].is_valid_password(user_pwd):
                return users[0]

        return None
