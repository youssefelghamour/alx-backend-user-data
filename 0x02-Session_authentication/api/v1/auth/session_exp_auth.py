#!/usr/bin/env python3
"""
SessionExpAuth class module
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class """

    def __init__(self):
        """ Initialization """
        super().__init__()
        try:
            duration = int(getenv("SESSION_DURATION", 0))
        except ValueError:
            duration = 0

        self.session_duration = duration

    def create_session(self, user_id=None):
        """ Creates a session for the user (with date of creation) """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns a User ID based on a Session ID """
        if not session_id:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None

        user_id = session_dict.get('user_id')
        if not user_id:
            return None

        if self.session_duration <= 0:
            return user_id

        created_at = session_dict.get('created_at')
        if not created_at:
            return None

        duration = timedelta(seconds=self.session_duration)
        if (created_at + duration) < datetime.now():
            return None

        return user_id
