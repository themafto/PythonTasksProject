def multiply_decorator(factor):
    def wrapper(func):
        def inner_wrapper():
            result = func()
            return result * factor
        return inner_wrapper
    return wrapper


@multiply_decorator(2)
def get_price():
    return 50

print(get_price())
