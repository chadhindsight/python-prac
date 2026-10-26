# First, we need to import re!
import re
# Define is_valid_time below:

def is_valid_time(input):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$')
    
    match = time_regex.search(input)
    
    if match:
        return True
    return False