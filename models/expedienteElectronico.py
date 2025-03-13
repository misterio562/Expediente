from models.cuaderno import Cuaderno
from models.procesoJudicial import ProcesoJudicial
from models.retencionDocumental import RetencionDocumental
from typing import List

class ExpedienteElectronico:
    def __init__(
        self,
        id: str,
        expediente_fisico: bool,
        soporte_fisico_expediente_judicial: bool,
        cuadernos: List[Cuaderno],
        proceso_judicial: ProcesoJudicial,
        retencion_documental: RetencionDocumental,
    ):
        self._id = id
        self._expediente_fisico = expediente_fisico
        self._soporte_fisico_expediente_judicial = soporte_fisico_expediente_judicial
        self._cuadernos = cuadernos
        self._proceso_judicial = proceso_judicial
        self._retencion_documental = retencion_documental

    def get_id(self):
        return self._id
    
    def set_id(self, id: str):
        self._id = id
    
    def get_expediente_fisico(self):
        return self._expediente_fisico
    
    def set_expediente_fisico(self, expediente_fisico: bool):
        self._expediente_fisico = expediente_fisico
    
    def get_soporte_fisico_expediente_judicial(self):
        return self._soporte_fisico_expediente_judicial
    
    def set_soporte_fisico_expediente_judicial(self, soporte_fisico_expediente_judicial: bool):
        self._soporte_fisico_expediente_judicial = soporte_fisico_expediente_judicial
    
    def get_cuadernos(self):
        return self._cuadernos
    
    def set_cuadernos(self, cuadernos: List[Cuaderno]):
        self._cuadernos = cuadernos

    def add_cuaderno(self, cuaderno: Cuaderno):
        if self._cuadernos is None:
            self._cuadernos = []
        self._cuadernos.append(cuaderno)
    
    def get_proceso_judicial(self):
        return self._proceso_judicial
    
    def set_proceso_judicial(self, proceso_judicial: ProcesoJudicial):
        self._proceso_judicial = proceso_judicial
    
    def get_retencion_documental(self):
        return self._retencion_documental
    
    def set_retencion_documental(self, retencion_documental: RetencionDocumental):
        self._retencion_documental = retencion_documental
    
    def delete(self):
        self._id = None
        self._expediente_fisico = None
        self._soporte_fisico_expediente_judicial = None
        self._cuadernos = []  
        self._proceso_judicial = None
        self._retencion_documental = None
    
    # Impresion tipo JSON
    def __str__(self):
        return f"Expediente Electrónico ---> ID: {self._id}, Expediente Físico: {self._expediente_fisico}, Soporte Físico Expediente Judicial: {self._soporte_fisico_expediente_judicial}, Cuadernos: {self._cuadernos}, Proceso Judicial: {self._proceso_judicial}, Retención Documental: {self._retencion_documental}\n"