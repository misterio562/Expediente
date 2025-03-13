from models.cuaderno import Cuaderno


class Documento:
    def __init__(
        self,
        codigo: int,
        nombre: str,
        fecha_creacion: str,
        fecha_incorporacion: str,
        orden: int,
        numero_paginas: int,
        pagina_inicio: int,
        pagina_final: int,
        formato: str,
        tamanio: str,
        origen: str,
        cuaderno: Cuaderno,
        observaciones: str,
    ):
        self._codigo = codigo
        self._nombre = nombre
        self._fecha_creacion = fecha_creacion
        self._fecha_incorporacion = fecha_incorporacion
        self._orden = orden
        self._numero_paginas = numero_paginas
        self._pagina_inicio = pagina_inicio
        self._pagina_final = pagina_final
        self._formato = formato
        self._tamanio = tamanio
        self._origen = origen
        self._cuaderno = cuaderno
        self._observaciones = observaciones
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo: int):
        self._codigo = codigo
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre
    
    def get_fecha_creacion(self):
        return self._fecha_creacion
    
    def set_fecha_creacion(self, fecha_creacion: str):
        self._fecha_creacion = fecha_creacion
    
    def get_fecha_incorporacion(self):
        return self._fecha_incorporacion
    
    def set_fecha_incorporacion(self, fecha_incorporacion: str):
        self._fecha_incorporacion = fecha_incorporacion
    
    def get_orden(self):
        return self._orden
    
    def set_orden(self, orden: int):
        self._orden = orden
    
    def get_numero_paginas(self):
        return self._numero_paginas
    
    def set_numero_paginas(self, numero_paginas: int):
        self._numero_paginas = numero_paginas
    
    def get_pagina_inicio(self):
        return self._pagina_inicio
    
    def set_pagina_inicio(self, pagina_inicio: int):
        self._pagina_inicio = pagina_inicio
    
    def get_pagina_final(self):
        return self._pagina_final
    
    def set_pagina_final(self, pagina_final: int):
        self._pagina_final = pagina_final
    
    def get_formato(self):
        return self._formato
    
    def set_formato(self, formato: str):
        self._formato = formato
    
    def get_tamanio(self):
        return self._tamanio
    
    def set_tamanio(self, tamanio: str):
        self._tamanio = tamanio
    
    def get_origen(self):
        return self._origen
    
    def set_origen(self, origen: str):
        self._origen = origen
    
    def get_cuaderno(self):
        return self._cuaderno
    
    def set_cuaderno(self, cuaderno: Cuaderno):
        self._cuaderno = cuaderno
    
    def get_observaciones(self):
        return self._observaciones
    
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    def delete(self):
        self._codigo = None
        self._nombre = None
        self._fecha_creacion = None
        self._fecha_incorporacion = None
        self._orden = None
        self._numero_paginas = None
        self._pagina_inicio = None
        self._pagina_final = None
        self._formato = None
        self._tamanio = None
        self._origen = None
        self._cuaderno = None
        self._observaciones = None
    
    def __str__(self) -> str:
        return self._nombre if self._nombre is not None else ""
