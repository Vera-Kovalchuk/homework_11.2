from collections.abc import Callable
from functools import wraps


def log(filename: str | None = None):
    """Декоратор может логировать начало и конец выполнения функции,
    ее результаты или ошибки."""

    def decorator(my_func: Callable):
        @wraps(my_func)
        def wrapper(*args, **kwargs):
            if not filename:
                print(f"{my_func.__name__} started")
                try:
                    my_func(*args, **kwargs)
                    print(f"{my_func.__name__} ok")
                    print(f"{my_func.__name__} finished")
                except Exception as e:
                    print(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                try:
                    my_func(*args, **kwargs)
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} ok")
                except Exception as e:
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator
