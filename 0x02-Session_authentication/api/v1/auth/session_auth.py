#!/usr/bin/env python3
"""
SessionAuth class module
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID """
        if not session_id or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User based on a cookie value (session id) """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Deletes the user session / logout """
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user = self.user_id_for_session_id(session_id)
        if not user:
            return False

        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]

        return True
