import requests
import socket

# Busca si hay una lista dentro de un dict
def hay_lista(diccionario):
    encontrado = False
    for key in diccionario:
        if isinstance(diccionario[key], list):
            encontrado = True
    return encontrado

# Buscamos diccionarios en la lista
def hay_dict_en_list(lista):
    encontrado = False
    for element in lista:
        if isinstance(element, dict):
            encontrado = True
    return encontrado

def search_key(response_json):
    for key in response_json:
        print(key)
    key_to_search = input('Introduce alguna de estas keys para saber su valor o pulsa INTRO\n' +
                            'para buscar las claves dentro de otro dict (si lo hay): ')
    if key_to_search == '':
        if hay_lista(response_json):
            # Pintamos los 'nombres' de cada lista
            print('Los valores de las siguientes keys son listas:')
            for key in response_json:
                if isinstance(response_json[key], list):
                    print(key)
            key_to_search = input('Introduce la key de la lista en la que\n' +
                                  'quieres buscar más dicts: ')
            # Ahora buscamos si en esa lista hay más dicts
            if hay_dict_en_list(response_json[key_to_search]):
                # Si los hay contamos los que hay
                cont_dict = 0
                for element in response_json[key_to_search]:
                    if isinstance(element, dict):
                        cont_dict +=1
                print("Hay " + str(cont_dict) + " diccionarios en " +
                      str(len(response_json[key_to_search])) + " elementos totales.")
    else:
        print(response_json[key_to_search])

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
    
    #print("El número de diccionarios es: ", read_dict(response_json, dict_ints, f)['Dict'],
    #      "\nEl número de listas es: ", dict_ints['Lista'],
    #      "\nEl número de tuplas es: ", dict_ints['Tupla'],
    #      "\nEl número de tipos primitivos es: ", dict_ints['Primitivo'],
    #      "\nEl número de ints es: ", dict_ints['Int'],
    #      "\nEl número de floats es: ", dict_ints['Float'],
    #      "\nEl número de strings es: ", dict_ints['String'])
    f.close()

    search_key(response_json)
    #print("El valor de la clave " + key_to_search + " es " + str(response_json[key_to_search]))
    