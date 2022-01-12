import re
import pyperclip


PHONE_NUMBER_REGEX = re.compile(r'''(
    (\+48)?          # Polish
    (\d{3})          # 1st 3 digits
    (\s|-)?          # separator
    (\d{3})          # 2nd 3 digits
    (\s|-)?          # separator
    (\d{3})          # 3rd 3 digits
    )''', re.VERBOSE)
