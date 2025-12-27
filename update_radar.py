import requests
import os
import json
import time

api_key = os.getenv("AEMET_API_KEY")
url_aemet = "https://opendata.aemet.es/opendata/api/red/radar/regional/va/"
headers = {'api_key': api_key}

def update():
    try:
        # 1. Pedir el enlace temporal
        r = requests.get(url_aemet, headers=headers)
        
        if r.status_code == 429:
            print("Límite de la API alcanzado. Esperando 10 segundos para reintentar...")
            time.sleep(10)
            r = requests.get(url_aemet, headers=headers)
            
        r.raise_for_status()
        temp_url = r.json()['datos']
        
        # 2. Descargar el JSON final
        # Importante: Este enlace NO requiere API Key
        r_datos = requests.get(temp_url)
        radar_final = r_datos.json()
        
        with open('radar_data.json', 'w') as f:
            json.dump(radar_final, f)
            
        print("Datos de Valencia actualizados correctamente.")
        
    except Exception as e:
        print(f"No se pudo actualizar: {e}")

if __name__ == "__main__":
    update()