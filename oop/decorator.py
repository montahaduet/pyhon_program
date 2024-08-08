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
        print(f'wrapper executed before')

