import re


# define parse_bytes below:
def parse_bytes(input):
    # Any combination of 0s or 1s repeated eight times
    byte_regex = re.compile(r'\b[01]{8}\b')
    
    result = byte_regex.findall(input)
    return result
        
