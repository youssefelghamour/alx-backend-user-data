#!/usr/bin/env python3
""" Module of session authentification
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login/
    JSON body:
      - email
      - password
    Return:
      - User object JSON represented
    """
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        # returns a list of user
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    user = users[0]

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())

    SESSION_NAME = getenv("SESSION_NAME")
    response.set_cookie(SESSION_NAME, session_id)

    return response
