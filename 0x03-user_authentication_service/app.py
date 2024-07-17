#!/usr/bin/env python3
""" Flask app """
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ GET /
        Return:
            JSON welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """ POST /users
        Registers a new user with the provided email and password

        Returns:
            JSON response indicating success or failure
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
