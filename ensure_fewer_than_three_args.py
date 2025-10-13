from functools import wraps

# From Colt's ting 
def ensure_fewer_than_three_args(fn):
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper