#!/usr/bin/env python3
"""
Auth class module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentification class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path """
        if not path or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            # if "path" or "path/" in excluded_paths
            # excluded_paths contains string path always ending by a /

            if (path.startswith(excluded_path) or
                    (path + "/").startswith(excluded_path)):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Placeholder method for retrieving authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Placeholder method for retrieving current user """
        return None
