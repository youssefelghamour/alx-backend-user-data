#!/usr/bin/env python3
"""
SessionAuth class module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authentification class """

    # this dict allows us to retrieve a User id based on a Session ID
    # {session_id1: user_id1, session_id2: user_id1, ...}
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id """
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
