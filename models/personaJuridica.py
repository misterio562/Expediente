from models.persona import Persona


class PersonaJuridica(Persona):
    def __init__(
        self,
        tipo_documento: str,
        numero_documento: int,
        nombre: str,
        razon_social: str,
        representante_legal: str,
    ):
        super().__init__(tipo_documento, numero_documento, nombre)
        self._tipo_documento = tipo_documento
        self._numero_documento = numero_documento
        self._nombre = nombre
        self._razon_social = razon_social
        self._representante_legal = representante_legal

    def __str__(self):
        return f"Persona Jurídica [Documento: {self._tipo_documento} {self._numero_documento}, Nombre: {self._nombre}, Razón Social: {self._razon_social}, Representante Legal: {self._representante_legal}]"
