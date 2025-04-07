# Return a copy of the list where each item has been decremented by one
def decrement_list(vals):
    tings = map(lambda num: num -1, vals)
    return list(tings)