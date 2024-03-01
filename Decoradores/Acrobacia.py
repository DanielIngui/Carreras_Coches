from functools import wraps

def acrobacia(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.velocidad_actual += 10
        result = func(self, *args, **kwargs)
        self.velocidad_actual -= 10
        return result
    return wrapper
