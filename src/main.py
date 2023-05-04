from functools import wraps
from timeit import default_timer


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"You called {func.__name__}{args}. It returned {result}.")
        return result

    return wrapper


def starred(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("************")
        func(*args, **kwargs)
        print("************")
    return wrapper


def count(func):
    dictionary = {func.__name__: 0}

    @wraps(func)
    def wrapper(*args, **kwargs):
        dictionary[func.__name__] += 1
        for key, value in dictionary.items():
            if value == 1:
                print(f"Function {key} was called {value} time.")
            else:
                print(f"Function {key} was called {value} times.")
        return func(*args, **kwargs)
    return wrapper


def arg_check(expected_type):
    def check(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(*args, expected_type):
                print(f"Expected type {expected_type} and got type {type(*args)}.")
                return func(*args, **kwargs)
            else:
                raise TypeError(f"Expected type {expected_type} but got type {type(*args)}.")
        return wrapper
    return check


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = default_timer()
        func(*args, **kwargs)
        stop = default_timer()
        duration = stop - start
        print(f"Function {func.__name__} lasted {duration} sec.")
        return func
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@count
@starred
def hello_world():
    print("Hello World!")


@time_this
@arg_check(float)
def plus_one(num):
    return num + 1


def main():
    func(4, 4, 4)
    hello_world()
    hello_world()
    plus_one(1.0)


if __name__ == '__main__':
    main()
