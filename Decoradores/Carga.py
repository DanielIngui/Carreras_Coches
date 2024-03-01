from functools import wraps

def carga(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        carga = args[0]  # Se asume que el primer argumento es la carga
        self.velocidad_maxima -= carga * 2
        result = func(self, *args, **kwargs)
        self.velocidad_maxima += carga * 2
        return result
    return wrapper
