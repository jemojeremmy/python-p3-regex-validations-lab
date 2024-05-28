import re

# Define the regular expressions
name_regex = re.compile(r"^[A-Z][a-zA-Z'-]*( [A-Z][a-zA-Z'-]*)*$")
phone_regex = re.compile(r"^(\d{10}|\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$")
email_regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]+$")
