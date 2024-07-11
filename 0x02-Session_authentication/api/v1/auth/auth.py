#!/usr/bin/env python3
"""
Auth class module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Authentification class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path

            - excluded_paths: Paths that do not require authentication

            Returns: True if path requires authentification, False otherwise
        """
        if not path or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path or (path + "/") == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header """
        if not request:
            return None

        headers = request.headers
        if 'Authorization' not in headers.keys():
            return None

        return headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Placeholder method for retrieving current user """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value (session id) from a request """
        if not request:
            return None

        _my_session_id = getenv("SESSION_NAME")

        session_cookie = request.cookies.get(_my_session_id)

        return session_cookie
