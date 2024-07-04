#!/usr/bin/env python3
""" module for obfuscating sensitive data in log messages """
import re


# () capture group that captures a specific pattern
# [] matches any one of the characters inside the brackets
# in this case, ^; translate literally to anything except semicolon
# (since ^ matches any character not listed in the brackets)
# + to capture more than one character (all chracters until we reach ;)


def filter_datum(fields, redaction, message, separator):
    """ function filter sensitive fields in a log message
        and obfuscate their values

        Arguments:
        - fields: a list of strings representing all fields to obfuscate
        - redaction: a string representing by what the field will be obfuscated
        - message: a string representing the log line
        - separator: a string representing by which character is separating all
                    fields in the log line (message)

        Returns:
        - modified_message: the log message with sensitive fields obfuscated
    """
    modified_message = message
    for field in fields:
        pattern = r'{}=([^{}]+)'.format(field, separator)
        modified_message = re.sub(pattern, '{}={}'.format(field, redaction),
                                  modified_message)
    return modified_message
