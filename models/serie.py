from models.tipoDocumental import TipoDocumental


class SubSerie:
    def __init__(self, codigo: int, nombre: str, tipo_documental: list[TipoDocumental]):
        self._codigo = codigo
        self._nombre = nombre
        self._tipo_documental = tipo_documental
    
    def get_codigo(self):
        return self._codigo
    
    def get_nombre(self):
        return self._nombre
    
    def get_tipo_documental(self):
        return self._tipo_documental
    
    def __str__(self):
        tipos = ", ".join(str(tipo) for tipo in self._tipo_documental)
        return f"SubSerie ---> Codigo: {self._codigo}, Nombre: {self._nombre}, Tipos Documentales: [{tipos}]"


class Serie:
    def __init__(self, codigo: int, nombre: str, sub_series: list[SubSerie]):
        self._codigo = codigo
        self._nombre = nombre
        self._sub_series = sub_series
    
    def get_codigo(self):
        return self._codigo
    
    def get_nombre(self):
        return self._nombre
    
    def get_sub_series(self):
        return self._sub_series
    
    def __str__(self):
        subseries = ", ".join(str(subserie) for subserie in self._sub_series)
        return f"Serie ---> Codigo: {self._codigo}, Nombre: {self._nombre}\nSub Series: [{subseries}]"