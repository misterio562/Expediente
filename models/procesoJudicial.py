from models.despachoJudicial import DespachoJudicial
from models.parteProcesal import ParteProcesal


class ProcesoJudicial:
    def __init__(
        self,
        numero_radicado: str,
        despacho_judicial: DespachoJudicial,
        parte_procesal: ParteProcesal,
    ):
        self._numero_radicado = numero_radicado
        self._despacho_judicial = despacho_judicial
        self._parte_procesal = parte_procesal
    
    def get_numero_radicado(self):
        return self._numero_radicado
    
    def set_numero_radicado(self, numero_radicado: str):
        self._numero_radicado = numero_radicado
    
    def get_despacho_judicial(self):
        return self._despacho_judicial
    
    def set_despacho_judicial(self, despacho_judicial: DespachoJudicial):
        self._despacho_judicial = despacho_judicial
    
    def get_parte_procesal(self):
        return self._parte_procesal
    
    def set_parte_procesal(self, parte_procesal: ParteProcesal):
        self._parte_procesal = parte_procesal
    
    def delete(self):
        self._numero_radicado = None
        self._despacho_judicial = None
        self._parte_procesal = None

    def __str__(self):
        return f"Proceso Judicial ---> Radicado: {self._numero_radicado}\n - Despacho Judicial: {self._despacho_judicial}\n - Parte Procesal: {self._parte_procesal}"
