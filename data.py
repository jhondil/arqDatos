#
import requests
import json
from database.db import InserDb

def run():

    dataCole=[]

    url = "https://www.datos.gov.co/resource/kgxf-xxbe.json?$limit=10000&periodo=20221"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    for d in data:
        InserDb.etl_data(
            d.get("estu_tipodocumento", "CC"),
            d.get("cole_area_ubicacion", "URBANO"),
            d.get("cole_bilingue", "N"),
            d.get("cole_depto_ubicacion", "VALLE"),
            d.get("cole_jornada", "COMPLETA"),
            d.get("estu_depto_reside", "VALLE"),
            d.get("estu_genero", "F"),
            d.get("estu_mcpio_presentacion", "CALI"),
            d.get("estu_mcpio_reside", "CALI"),
            d.get("fami_estratovivienda", "Estrato 3"),
            d.get("desemp_ingles", "A0"),
            int(d.get("punt_ingles", 0)),
            int( d.get("punt_matematicas", 0)),
            int(d.get("punt_sociales_ciudadanas", 0)),
            int(d.get("punt_c_naturales", 0)),
            int(d.get("punt_lectura_critica", 0)),
            int(d.get("punt_global", 0)) 
            )
        # dataCole.append(d["cole_nombre_sede"))
    # print(len(dataCole))
            # print(d["estu_tipodocumento"))
            # print(d["cole_area_ubicacion"])
            # print(d["cole_bilingue"])
            # print(d["cole_depto_ubicacion"])
            # print(d["cole_jornada"])
            # print(d["estu_depto_reside"])
            # print(d["estu_genero"])
            # print(d["estu_mcpio_presentacion"])
            # print(d["estu_mcpio_reside"])
            # print(d["fami_estratovivienda"])
            # print(d["desemp_ingles"])
            # print(int(d["punt_ingles"]))
            # print(int( d["punt_matematicas"]))
            # print(int(d["punt_sociales_ciudadanas"]))
            # print(int(d["punt_c_naturales"]))
            # print(int(d["punt_lectura_critica"]))
            # print(int(d["punt_global"]))


if __name__ == "__main__":  # entrypoint
    run()

        
        # "estu_tipodocumento": "CC",
        
        # "cole_area_ubicacion": "URBANO",
        # "cole_bilingue": "N",
        
        # "cole_depto_ubicacion": "VALLE",
       
        # "cole_jornada": "COMPLETA",
   
        # "estu_depto_reside": "VALLE",
        
        # "estu_genero": "F",
        # "estu_mcpio_presentacion": "CALI",
        # "estu_mcpio_reside": "CALI",
       

        # "fami_estratovivienda": "Estrato 4",
       
        # "desemp_ingles": "A1",
        # "punt_ingles": "54",
        # "punt_matematicas": "47",
        # "punt_sociales_ciudadanas": "64",
        # "punt_c_naturales": "51",
        # "punt_lectura_critica": "66",
        # "punt_global": "284"





