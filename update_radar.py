import requests
import os
import json

api_key = os.getenv("AEMET_API_KEY")
url_aemet = "https://opendata.aemet.es/opendata/api/observacion/radar/nacional"

headers = {'api_key': api_key}

try:
    print("Conectando con AEMET...")
    r = requests.get(url_aemet, headers=headers)
    r.raise_for_status() # Esto lanzará un error si la API Key está mal
    
    res_inicial = r.json()
    print(f"Respuesta AEMET: {res_inicial['descripcion']}")
    
    endpoint_datos = res_inicial['datos']
    
    print("Descargando JSON final de datos...")
    r_datos = requests.get(endpoint_datos)
    datos_finales = r_datos.json()
    
    # Verificamos que tenemos el enlace de la imagen
    if 'enlace' in datos_finales:
        with open('radar_data.json', 'w') as f:
            json.dump(datos_finales, f)
        print("¡Archivo radar_data.json guardado correctamente!")
    else:
        print("Error: El JSON de datos no contiene el campo 'enlace'")

except Exception as e:
    print(f"ERROR CRÍTICO: {e}")
    # Si hay error, no guardamos un archivo vacío