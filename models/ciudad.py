class Ciudad:
    def __init__(self, nombre: str):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre
    
    def delete(self):
        self._nombre = None

    def __str__(self):
        return f"  - Nombre: {self._nombre}"
