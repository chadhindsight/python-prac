# A more Python-ic solution involves using a list comprehension to do the same thing on a single line. Both work just as well.  
# It's a matter of personal preference, so don't get too caught up in it!



def intersection(l1, l2):
    return [val for val in l1 if val in l2]