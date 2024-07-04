#!/usr/bin/env python3
""" module for obfuscating sensitive data in log messages """
import re


def filter_datum(fields, redaction, message, separator):
    """ function filter sensitive fields in a log message """
    return re.sub(r'({})=([^{}]+)'.format('|'.join(fields), separator),
                  r'\1={}'.format(redaction), message)
