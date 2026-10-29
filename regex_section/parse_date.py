import re

#define parse_date below
def parse_date(input):
    date_regex = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    
    # Alternative way to to write the date_regex
    # date_regex = re.compile(r"^(\d{2})[,/.](\d{2})[,/.](\d{4})$")

    match = date_regex.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None    
        