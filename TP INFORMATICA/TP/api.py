# import requests
import requests
import json

api_url = 'https://100k-faces.glitch.me/'

def obtener_foto():
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.text
            if 'src' in data:
                return data[1005:1046]
    except Exception as e:
        print(f"Error en la solicitud a la API: {e}")
    return None
obtener_foto()