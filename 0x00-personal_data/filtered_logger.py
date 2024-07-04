#!/usr/bin/env python3
""" module for obfuscating sensitive data in log messages """
import re


# () capture group that captures a specific pattern
# [] matches any one of the characters inside the brackets
# in this case, ^; translate literally to anything except semicolon
# (since ^ matches any character not listed in the brackets)
# + to capture more than one character (all chracters until we reach ;)


def filter_datum(fields, redaction, message, separator):
    """ function filter sensitive fields in a log message """
    for field in fields:
        pattern = r'{}=([^{}{}]+)'.format(field, separator, separator)
        message = re.sub(pattern, '{}={}'.format(field, redaction), message)
    return message
