#!/usr/bin/env python3
""" module for obfuscating sensitive data in log messages """
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ creates and returns a MySQL database connection """
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )
    return connection


def get_logger() -> logging.Logger:
    """ returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function filter sensitive fields in a log message """
    for field in fields:
        pattern = r'{}=([^{}]+)'.format(field, separator)
        message = re.sub(pattern, '{}={}'.format(field, redaction), message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filters and formats a record """
        # Filter sensitive fields in the log record message
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)

        # Apply the custom format defined in self.FORMAT to the record
        # Accessing the format method of the superclass (logging.Formatter)
        # that has our self.FORMAT that we initalized it with in init
        formatted_record = super().format(record)

        return formatted_record


def main():
    """ filteres user data from a database """
    # Get logger with RedactingFormatter
    logger = get_logger()

    # Obtain database connection
    db = get_db()

    # Fetch all rows from users table
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    # Example: rows fetched from the database
    # rows = [
    #     {'name': 'ysf', 'email': 'ysf@example.com', 'phone': '123',
    #      'ssn': '14-89', 'password': 'sdkjb', 'ip': '192.168.1.1',
    #      'last_login': '2023-01-01 12:00:00', 'user_agent': 'Mozilla/5.0'},
    #
    #     {'name': 'some user', 'email': 'user@example.com', ...}
    # ]

    # Close database connection
    db.close()

    # Log each row with sensitive information redacted using the logger
    for row in rows:
        # Each row is a dictionary
        # Convert row dictionary to a formatted string
        msg = "; ".join(f"{key}={value}" for key, value in row.items())
        msg += ";"

        # Create a log record with the formatted message
        record = logging.LogRecord("user_data", logging.INFO, None, None,
                                   msg, None, None)

        # Log the formatted message using the logger
        logger.handle(record)


if __name__ == "__main__":
    main()
