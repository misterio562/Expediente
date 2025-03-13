from models.persona import Persona


class PersonaNatural(Persona):
    def __init__(self, tipo_documento: str, numero_documento: int, nombre: str):
        super().__init__(tipo_documento, numero_documento, nombre)
        self._tipo_documento = tipo_documento
        self._numero_documento = numero_documento
        self._nombre = nombre

    def __str__(self):
        return f"Persona Natural [Documento: {self._tipo_documento} {self._numero_documento}, Nombre: {self._nombre}]"
