import time
from functools import wraps

def time_elapsed(func):
    @wraps(func)  #1
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        print('time elapsed executing a `{}` function : {:.2f}s'.format(func.__name__, time.time() - start_time))

        return res

    return wrapper
