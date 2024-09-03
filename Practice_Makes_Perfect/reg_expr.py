# https://regex101.com/
import re

# Create a password that is 8 chars long and ends with a number
pattern = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
password = "blahdjdjd1112"
check = pattern.fullmatch(password)
print(check)