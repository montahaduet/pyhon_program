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

#non keyword arguments=>f(1,2,3)
# keyword arguments=>f(a=1,b=2,c=3)
def decorator_2(original_func):

    print('in the decorator_2 function\n')

    def wrapper(*args,**kwargs):
        print(f'wrapper executed before{original_func.__name__}()')

        if 10>5:
            print('yes it is true')
        return original_func(*args,**kwargs)

    return wrapper


# using decorator in one way

@decorator
def print_something():
    print('print_something is being ran!')
print_something()

@decorator_2
def print_something_more(arg1,arg2):
    print(f'printing argument_1={arg1} and argument_2={arg2}')

print_something_more(3,5)
# decorator_f=decorator(print_something)
# decorator_f()

