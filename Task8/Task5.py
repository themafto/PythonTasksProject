def double_decorator(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper

def add_five_decorator(func):
    def wrapper():
        result = func() + 5
        return result
    return wrapper

@add_five_decorator
@double_decorator
def get_value():
    return 5

print(get_value())