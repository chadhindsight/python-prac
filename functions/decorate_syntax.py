# NB: decorators are functions that wrap other functions
def be_nice(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_nice
def greet():
    print("My name is Colt")


@be_nice
def rage():
	print("I HATE YOU!")


greet()
rage()
