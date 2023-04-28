import requests
import socket

def is_primitive(data):
    return isinstance(data, int) or isinstance(data, str) or isinstance(data, float)

# Recorre el mapa y cuenta el número de dicts anidados
def read_dict(data_dict, dict_ints, f):
    print("ENTRAMOS EN UN DICCIONARIO")
    for key in data_dict:
        if is_primitive(data_dict[key]):
            dict_ints['Primitivo'] +=1
            if isinstance(data_dict[key], int):
                dict_ints['Int'] +=1
            elif isinstance(data_dict[key], str):
                dict_ints['String'] +=1
                #f.write(str('String => Clave: ' + str(key) + '\nValor: ' + data_dict[key] + '\n'))
            elif isinstance(data_dict[key], float):
                dict_ints['Float'] +=1
        elif isinstance(data_dict[key], tuple):
            dict_ints['Tupla'] +=1
        elif isinstance(data_dict[key], list):
            dict_ints['Lista'] +=1
            for element in data_dict[key]:
                if isinstance(element, dict):
                    dict_ints['Dict'] +=1
                    print("LLEVAMOS ",read_dict(element, dict_ints, f))
    return dict_ints
                

if __name__ == "__main__":

    url = "https://api.publicapis.org/entries"
    dict_ints = {'Primitivo': 0,'Int': 0, 'String': 0, 'Float': 0, 'Tupla': 0, 'Lista': 0, 'Dict': 1}
    # Archivo de prueba
    f = open("datos.txt", "a")
    socket.getaddrinfo('22.88.107.0', 8080)
    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    #print(response_json)
    print("===================================")
    
    print("El número de diccionarios es: ", read_dict(response_json, dict_ints, f)['Dict'],
          "\nEl número de listas es: ", dict_ints['Lista'],
          "\nEl número de tuplas es: ", dict_ints['Tupla'],
          "\nEl número de tipos primitivos es: ", dict_ints['Primitivo'],
          "\nEl número de ints es: ", dict_ints['Int'],
          "\nEl número de floats es: ", dict_ints['Float'],
          "\nEl número de strings es: ", dict_ints['String'])
    f.close()
    