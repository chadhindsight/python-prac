import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    censored_result = pattern.sub("CENSORED", input) 
    return censored_result 
