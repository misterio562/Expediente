class TipoDocumental:
    def __init__(self, codigo: int, nombre: str):
        self._codigo = codigo
        self._nombre = nombre

    def get_codigo(self):
        return self._codigo
    
    def get_nombre(self):
        return self._nombre
    
    def __str__(self):
        return f"Tipo Documental ---> Codigo: {self._codigo}, Nombre: {self._nombre}"
