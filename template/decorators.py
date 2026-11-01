import functools

TASKS = []


def task_skipper(skip):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if skip:
                print(f"Skipping...")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator


def task(desc=""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        TASKS.append((desc, wrapper))
        return wrapper
    return decorator
