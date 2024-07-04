#!/usr/bin/env python3
""" module for obfuscating sensitive data in log messages """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function filter sensitive fields in a log message """
    for field in fields:
        pattern = r'{}=([^{}]+)'.format(field, separator)
        message = re.sub(pattern, '{}={}'.format(field, redaction), message)
    return message
