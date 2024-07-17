#!/usr/bin/env python3
"""Authentification module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ hashes a password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
