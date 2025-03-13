from almacenamiento.cuadernoYdocumentos import CUADERNOS, DOCUMENTOS
from almacenamiento.parteProcesal import PARTEA, PARTEB
from almacenamiento.procesoJudicial import PROCESOS_JUDICIALES
from almacenamiento.retencionDocumental import SERIES
from models.ciudad import Ciudad
from models.departamento import Departamento
from models.categoria import Categoria
from models.despachoJudicial import DespachoJudicial
from models.expedienteElectronico import ExpedienteElectronico
from models.personaJuridica import PersonaJuridica
from models.personaNatural import PersonaNatural
from models.parteProcesal import ParteProcesal
from models.procesoJudicial import ProcesoJudicial
from models.retencionDocumental import RetencionDocumental
from models.tipoDocumental import TipoDocumental
from models.serie import Serie, SubSerie
from models.cuaderno import Cuaderno
from models.documento import Documento
from exportar_expediente import exportar_expediente_a_excel

if __name__ == "__main__":
    # Creación del Despacho Judicial
    ciudad1 = Ciudad("Bogotá")
    departamento1 = Departamento("Cundinamarca")
    categoria = Categoria("Municipal")
    despacho1 = DespachoJudicial("1", "Bogotá", departamento1, ciudad1, categoria)
    print(despacho1)
    
    # Creación del Parte Procesal
    personaJudicial1 = PersonaJuridica("CC", 1054343266,"Juan", "Meta", "Zuckerberg")
    personaNatural1 = PersonaNatural("CC", 49765884,"Julio")
    PARTEA.append(personaJudicial1) # Demandado
    PARTEB.append(personaNatural1) # Demandante
    parteProcesal = ParteProcesal(PARTEA, PARTEB)
    print(parteProcesal)

    # Creación del Proceso Judicial
    proceso1 = ProcesoJudicial("1", despacho1, parteProcesal)
    print(proceso1)
    PROCESOS_JUDICIALES.append(proceso1)
    
    # Retención Documental
    tipoDocumental1 = TipoDocumental(1, "Acciones de Tutela")
    tipoDocumental2 = TipoDocumental(2, "Acta de Reparto")
    tipoDocumental3 = TipoDocumental(3, "Auto que admite tutela")
    tipoDocumental4 = TipoDocumental(4, "Fallo de tutela")
    tipoDocumental5 = TipoDocumental(5, "Notificación de Tutela")
    tipoDocumental6 = TipoDocumental(6, "Solicitud de Desacato")
    tipoDocumental7 = TipoDocumental(7, "Desacato")
    tipoDocumental8 = TipoDocumental(8, "Notificación de Desacato")
    tipoDocumental9 = TipoDocumental(9, "Sentencia Revisión Corte Constitucional")
    
    subserie1 = SubSerie(1, "Subserie 1", [tipoDocumental1, tipoDocumental2])
    subserie2 = SubSerie(2, "Subserie 2", [tipoDocumental3, tipoDocumental4, tipoDocumental5])
    SERIES.append(subserie1)
    SERIES.append(subserie2)
    
    serie1 = Serie(1, "Serie 1", SERIES)
    retencion_documental = RetencionDocumental(1, serie1)

    # Cuaderno Y documento
    cuaderno1 = Cuaderno(1, "Principal" )
    cuaderno2 = Cuaderno(2, "Medias Previas")
    CUADERNOS.append(cuaderno1)
    CUADERNOS.append(cuaderno2)

    documento1 = Documento(1, tipoDocumental1.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Digitalizado", cuaderno1, "" )
    documento2 = Documento(2, tipoDocumental2.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno2, "" )
    documento3 = Documento(3, tipoDocumental3.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno1, "" )
    documento4 = Documento(4, tipoDocumental4.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno2, "" )
    documento5 = Documento(5, tipoDocumental5.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno1, "" )
    documento6 = Documento(6, tipoDocumental6.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Digitalizado", cuaderno2, "" )
    documento7 = Documento(7, tipoDocumental7.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno1, "" )
    documento8 = Documento(8, tipoDocumental8.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno2, "" )
    documento9 = Documento(9, tipoDocumental9.get_nombre(), "1/07/2020","1/07/2020", 1,5,1,5, "PDF", "783KB", "Electrónico", cuaderno1, "" )

    # Agregar documentos a la lista DOCUMENTOS
    DOCUMENTOS.append(documento1)
    DOCUMENTOS.append(documento2)
    DOCUMENTOS.append(documento3)
    DOCUMENTOS.append(documento4)
    DOCUMENTOS.append(documento5)
    DOCUMENTOS.append(documento6)
    DOCUMENTOS.append(documento7)
    DOCUMENTOS.append(documento8)
    DOCUMENTOS.append(documento9)
    print("\nDocumentos creados:")
    for doc in DOCUMENTOS:
        print(f" - {doc}")
    # Expediente Electrónico
    expediente1 = ExpedienteElectronico("1", True, True, CUADERNOS, proceso1, retencion_documental)
    print(expediente1)

    # Exportar expediente a Excel
    ruta_excel = "expediente_electronico.xlsx"
    exportar_expediente_a_excel(expediente1, ruta_excel)