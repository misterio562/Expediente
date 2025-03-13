import pandas as pd
from typing import Dict, List, Optional
from models.expedienteElectronico import ExpedienteElectronico
from models.documento import Documento
from models.cuaderno import Cuaderno
from almacenamiento.cuadernoYdocumentos import DOCUMENTOS


def exportar_expediente_a_excel(expediente: ExpedienteElectronico, ruta_archivo: str) -> None:
    """Exporta la información del expediente a un archivo Excel"""
    if not expediente._proceso_judicial or not expediente._proceso_judicial._despacho_judicial:
        raise ValueError("El expediente debe tener un proceso judicial y despacho judicial válidos")

    if not expediente._retencion_documental or not expediente._retencion_documental._serie:
        raise ValueError("El expediente debe tener una retención documental y serie válidas")

    # Información general del expediente
    info_general = {
        "Ciudad": expediente._proceso_judicial._despacho_judicial._ciudad.get_nombre(),
        "Despacho Judicial": expediente._proceso_judicial._despacho_judicial._nombre,
        "Serie": expediente._retencion_documental._serie._nombre,
        "Número de Radicado": expediente._proceso_judicial._numero_radicado,
        "Expediente Físico": "Sí" if expediente._expediente_fisico else "No",
        "Cantidad de Cuadernos": len(expediente._cuadernos) if expediente._cuadernos else 0,
    }
    
    # Información de las partes procesales
    if expediente._proceso_judicial._parte_procesal:
        parte_a = expediente._proceso_judicial._parte_procesal._parteA or []
        parte_b = expediente._proceso_judicial._parte_procesal._parteB or []
    else:
        parte_a = []
        parte_b = []
    
    info_partes = {
        "Parte A (Demandados)": ", ".join(str(p) for p in parte_a),
        "Parte B (Demandantes)": ", ".join(str(p) for p in parte_b),
    }
    
    # Crear el archivo Excel
    writer = pd.ExcelWriter(ruta_archivo, engine='xlsxwriter')
    
    # Hoja 1: Información General
    df_general = pd.DataFrame([{**info_general, **info_partes}])
    df_general.to_excel(writer, sheet_name='Información General', index=False)
    
    # Hoja 2: Documentos
    documentos = []
    # Buscamos todos los documentos que pertenecen a alguno de los cuadernos del expediente
    for cuaderno in expediente._cuadernos:
        for documento in DOCUMENTOS:
            if documento._cuaderno == cuaderno:
                documentos.append({
                    "Código": documento._codigo,
                    "Nombre": documento._nombre,
                    "Fecha Creación": documento._fecha_creacion,
                    "Fecha Incorporación": documento._fecha_incorporacion,
                    "Orden": documento._orden,
                    "Número Páginas": documento._numero_paginas,
                    "Página Inicio": documento._pagina_inicio,
                    "Página Final": documento._pagina_final,
                    "Formato": documento._formato,
                    "Tamaño": documento._tamanio,
                    "Origen": documento._origen,
                    "Cuaderno": documento._cuaderno._descripcion,
                    "Observaciones": documento._observaciones or ""
                })
    
    df_documentos = pd.DataFrame(documentos) if documentos else pd.DataFrame()
    if not df_documentos.empty:
        df_documentos.to_excel(writer, sheet_name='Documentos', index=False)
    
        # Ajustar el ancho de las columnas
        for sheet in writer.sheets.values():
            for i, col in enumerate(df_general.columns):
                sheet.set_column(i, i, len(str(col)) + 5)
            for i, col in enumerate(df_documentos.columns):
                sheet.set_column(i, i, len(str(col)) + 5)
    
    writer.close()
    print(f"Archivo Excel creado exitosamente en: {ruta_archivo}")
