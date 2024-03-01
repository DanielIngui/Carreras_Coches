from functools import wraps

def turbo(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.velocidad_maxima += 20
        result = func(self, *args, **kwargs)
        self.velocidad_maxima -= 20
        return result
    return wrapper
