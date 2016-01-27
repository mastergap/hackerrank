from time import time
from functools import wraps

def measure_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t = time()
        result = f(*args, **kwargs)
        print(f.__name__, 'took:{:.8f}'.format(time() - t))
        return result
    return wrapper