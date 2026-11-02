import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    result = pattern.sub("CENSORED", input) 
    return result 