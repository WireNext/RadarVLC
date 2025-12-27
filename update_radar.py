import requests
import os
import json

# Obtener la API Key desde los Secrets de GitHub
api_key = os.getenv("AEMET_API_KEY")
url_aemet = "https://opendata.aemet.es/opendata/api/observacion/radar/nacional"

headers = {'api_key': api_key}

try:
    # 1. Pedir el enlace de descarga
    r = requests.get(url_aemet, headers=headers)
    endpoint_datos = r.json()['datos']
    
    # 2. Obtener la URL final de la imagen y los límites
    r_datos = requests.get(endpoint_datos)
    datos_finales = r_datos.json()
    
    # 3. Guardar la URL de la imagen y metadatos en un archivo local
    with open('radar_data.json', 'w') as f:
        json.dump(datos_finales, f)
        
    print("Datos del radar actualizados con éxito.")
except Exception as e:
    print(f"Error: {e}")