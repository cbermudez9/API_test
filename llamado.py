import requests

def api_llamado():

    api_url = "https://rickandmortyapi.com/api/character/?status=alive"

    response = requests.get(api_url) #peticion get y guardado
    print("Respuesta: " + str(response.status_code)) #impresion del status code
    print("Tiempo de respuesta: " + str(response.elapsed.total_seconds())) #impresion del tiempo de respuesta
    cadena = str(response.json()) #casteo al objeto json para hacerlo cadena
    return cadena
