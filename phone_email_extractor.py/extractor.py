import re
import pyperclip


PHONE_NUMBER_REGEX = re.compile(r'''(
    (\+48)?                # Polish country code
    (\d{3})                # 1st 3 digits
    (\s|-)?                # separator
    (\d{3})                # 2nd 3 digits
    (\s|-)?                # separator
    (\d{3})                # 3rd 3 digits
    )''', re.VERBOSE)
EMAIL_REGEX = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)
