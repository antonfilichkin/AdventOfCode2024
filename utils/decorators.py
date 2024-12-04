import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        units = 'seconds'
        if elapsed_time < 1:
            elapsed_time *= 1000
            units = 'milliseconds'
        print(f"{func.__name__} took {elapsed_time:.2f} {units} to run")
        return result
    return wrapper
