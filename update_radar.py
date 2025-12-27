import requests
import os
import json

# Tu API Key guardada en Secrets
api_key = os.getenv("AEMET_API_KEY")

# URL específica para el radar de Valencia que me has pasado
url_aemet = "https://opendata.aemet.es/opendata/api/red/radar/regional/va/"

headers = {'api_key': api_key}

try:
    # 1. Pedir el enlace temporal (lo que me has pegado en el mensaje)
    r = requests.get(url_aemet, headers=headers)
    r.raise_for_status()
    temp_url = r.json()['datos']
    
    # 2. Descargar el JSON real con el enlace a la imagen .png
    r_datos = requests.get(temp_url)
    radar_final = r_datos.json()
    
    # 3. Guardar esto en tu repo para que el HTML lo lea
    with open('radar_data.json', 'w') as f:
        json.dump(radar_final, f)
        
    print("Datos de Valencia actualizados.")
except Exception as e:
    print(f"Error: {e}")