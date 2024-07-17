#!/usr/bin/env python3
"""Authentification module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ hashes a password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """ generates a new uuid """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user with the given email and password """
        try:
            # check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # user doesn't exist, proceed to create a new user
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ validates login credentials """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ creates a new session for a user """
        try:
            user = self._db.find_user_by(email=email)

            new_session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=new_session_id)

            return new_session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ finds user by session Id """
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

        return None
