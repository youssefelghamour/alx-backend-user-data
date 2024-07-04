#!/usr/bin/env python3
""" module for obfuscating sensitive data in log messages """
import re
from typing import List
import logging


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
