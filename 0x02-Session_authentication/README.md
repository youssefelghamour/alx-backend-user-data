# 0x02. Session authentication - API

HTTP API designed for managing user data and authentication within a Flask application. This API provides endpoints for user management and employs various authentication mechanisms, including basic authentication and session-based authentication with support for session expiration and database storage.

## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model
- `user_session.py`: model for user sessions stored in the database

### `api/v1`

- `app.py`: entry point of the API
- `views/`
  - `index.py`: basic endpoints of the API: `/status` and `/stats`
  - `users.py`: all users endpoints
  - `session_auth.py`: login and logout endpoints
- `auth/`
  - `auth.py`: base class for authentication
  - `basic_auth.py`: basic authentication logic
  - `session_auth.py`: session authentication logic
  - `session_db_auth.py`: authentication based on session IDs stored in the database
  - `session_exp_auth.py`: session expiration authentication logic


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
- `POST /api/v1/auth_session/login`: logs in a user and returns a session ID cookie
- `DELETE /api/v1/auth_session/logout`: logs out the user and deletes the session ID from the database
