from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    # this wrapper uses both arguments and keyword arguments
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper
