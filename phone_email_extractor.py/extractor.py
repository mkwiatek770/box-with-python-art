"""
Script that extract all phone numbers and email addresses from text.

How to use: 
1. CTRL+C to copy text to lookup.
2. Execute the program.
3. CTRL+V will paste all findings. 
"""
# TODO: split into functions
# TODO: tests
# TODO: wrap code by while loop to allow more than one extraction

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

 # Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in PHONE_NUMBER_REGEX.findall(text):
       phone_num = '-'.join([groups[2], groups[4], groups[6]])
       matches.append(phone_num)
for groups in EMAIL_REGEX.findall(text):
       matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
