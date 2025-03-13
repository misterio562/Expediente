class Cuaderno:
    def __init__(self, numero: int, descripcion: str):
        self._numero = numero
        self._descripcion = descripcion
    
    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero: int):
        self._numero = numero
    
    def get_descripcion(self):
        return self._descripcion
    
    def set_descripcion(self, descripcion: str):
        self._descripcion = descripcion
    
    def delete(self):
        self._numero = None
        self._descripcion = None
    
    def __str__(self):
        return f"Cuaderno ---> Número: {self._numero}, Descripción: {self._descripcion}"
