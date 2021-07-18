#! /usr/bin/python3
# extract phone number and e-mails from a section in string.
import re,pyperclip
text=pyperclip.paste()
phoneRegex=re.compile(r'''(
     (\d{3}|\(\d{3}\))?
     (\s|-|\.)?
     (\d{3})
     (\s|-|\.)
     (\d{4})
     (\s*(ext|x|ext\.)\s*(\d{2,5}))?
     )''',re.VERBOSE)
