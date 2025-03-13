from models.serie import Serie


class RetencionDocumental:
    def __init__(self, codigo: int, serie: Serie):
        self._codigo = codigo
        self._serie = serie
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo: int):
        self._codigo = codigo
    
    def get_serie(self):
        return self._serie
    
    def set_serie(self, serie: Serie):
        self._serie = serie
    
    def delete(self):
        self._codigo = None
        self._serie = None
    
    def __str__(self):
        return f"Retención Documental ---> Código: {self._codigo}, Serie: {self._serie}"
