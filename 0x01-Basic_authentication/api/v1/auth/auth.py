#!/usr/bin/env python3
"""
Auth class module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentification class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path

            - excluded_paths: Paths that do not require authentication

            Returns: True if path requires authentification, False otherwise
        """
        if not path or not excluded_paths:
            return True

        # for excluded_path in excluded_paths:
            # if "path" or "path/" in excluded_paths
            # excluded_paths contains string path always ending by a /

            # if (path.startswith(excluded_path) or
            #       (path + "/").startswith(excluded_path)):
            #    return False

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                # Create regex pattern for paths ending with '*'
                #   excluded_path[:-1] removes the * at the end
                #   + r'.*' match any number of any characters
                #   re.compile compiles it into a regex for matching
                regex = re.compile(excluded_path[:-1] + r'.*')

                if regex.fullmatch(path):
                    return False
            else:
                if path == excluded_path:
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
