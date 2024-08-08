def outer(message):
    print('In the outer function')

    def inner():
        print('calling the inner function')
        print(message)
    return inner

f=outer('Hello word')
print(f)    

def decorator(original_func):

    print('in the decorator function\n')

    def wrapper():
        print(f'wrapper executed before{original_func.__name__}()')

        if 10>5:
            print('yes it is true')
        return original_func()

    return wrapper


# using decorator in one way
def print_something():
    print('print_something is being ran!')

decorator_f=decorator(print_something)
decorator_f()

