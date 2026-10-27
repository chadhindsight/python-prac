import re


# define parse_bytes below:
def parse_bytes(input):
    byte_regex = re.compile(r'\b[01]{8}\b')
    result = byte_regex.findall(input)
    return result
        
