from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        valDem = fn(*args, **kwargs)
        return [valDem, valDem]
    return wrapper
