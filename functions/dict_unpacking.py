def display_names(first, second):
    print(f"{first} says hello to {second}")
names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..
display_names(**names)  # yup!

def add_and_multiply_numbers(val1,val2,val3,**kwargs):
    print(val1 + val2 * val3)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(val1=1,val2=2,val3=3,d=55,name="Tony")

print(add_and_multiply_numbers(**data))

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final
