from models.departamento import Departamento
from models.ciudad import Ciudad
from models.categoria import Categoria


class DespachoJudicial:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        departamento: Departamento,
        ciudad: Ciudad,
        categoria: Categoria,
    ):
        self._codigo = codigo
        self._nombre = nombre
        self._departamento = departamento
        self._ciudad = ciudad
        self._categoria = categoria

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_departamento(self):
        return self._departamento

    def get_ciudad(self):
        return self._ciudad

    def get_categoria(self):
        return self._categoria

    def set_codigo(self, codigo: str):
        self._codigo = codigo
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre
    
    def set_departamento(self, departamento: Departamento):
        self._departamento = departamento
    
    def set_ciudad(self, ciudad: Ciudad):
        self._ciudad = ciudad
    
    def set_categoria(self, categoria: Categoria):
        self._categoria = categoria
    
    # Impresion tipo JSON
    def __str__(self):
        return f" Despacho Judicial ---> Código: {self._codigo}, Nombre: {self._nombre}, Departamento: {self._departamento.get_nombre()}, Ciudad: {self._ciudad.get_nombre()}, Categoría: {self._categoria.get_nombre()}\n"
