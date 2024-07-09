# 0x00. Personal data

## Overview
This project involves handling personal data securely in a back-end application. It covers tasks such as logging, password encryption, and database connections with a focus on ensuring the security and privacy of Personally Identifiable Information (PII).

## File Table
| Filename                  | Description                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------|
| `filtered_logger.py`      | Contains functions and classes for logging, including obfuscating PII fields and creating a secure logger. |
| `encrypt_password.py`     | Contains functions for hashing passwords and validating them.                               |

## Methodology
This project focuses on the following key areas:
1. **Logging**: Implementing custom loggers that obfuscate PII data.
2. **Password Management**: Hashing passwords securely and validating them.
3. **Database Security**: Connecting to a database securely using environment variables for credentials.

## Process
1. **Regex-ing**: Using regular expressions to obfuscate sensitive fields in log messages.
2. **Log Formatter**: Creating a custom log formatter to filter out PII fields.
3. **Create Logger**: Setting up a logger that uses the custom formatter.
4. **Database Connection**: Connecting to a MySQL database securely using environment variables.
5. **Read and Filter Data**: Retrieving and filtering data from the database.
6. **Password Encryption**: Hashing and validating passwords using bcrypt.
