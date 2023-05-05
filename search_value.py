import requests
import socket

# Buscamos diccionarios en la lista
def hay_dict_en_list(lista):
    encontrado = False
    for element in lista:
        if isinstance(element, dict):
            encontrado = True
    return encontrado

def get_list_key(diccionario):
    for key in diccionario:
        if isinstance(diccionario[key], list):
            return key
        
def get_dict_index(lista):
    index = 0
    for element in lista:
        if isinstance(element, dict):
            return index
        else:
            index += 1

def search_dict(diccionario, key, value):
    if str(diccionario[key]).upper() == str(value).upper():
        print(diccionario)

def search_value(map):
    cont_list = 0
    for key in map:
        if isinstance(map[key], list):
            cont_list += 1
    
    if cont_list != 0:
        print("Hay lista, pasamos a buscar si hay un dict en ella")
        if hay_dict_en_list(map[get_list_key(map)]):
            print("Hay dict")
            lista = map[get_list_key(map)]
            # Ofrecemos al usuario las diferentes keys que hay en el diccionario
            print("El diccionario tiene las siguientes Keys")
            for key in lista[get_dict_index(lista)]:
                print(key)
            # Le preguntamos la key y el value para buscar en todos los dicts
            key_to_search = input("Elige la key en la que quieres buscar un valor: ")
            print("Has elegido " + key_to_search)
            value_to_search = input("¿Qué valor quieres buscar? ")
            for diccionario in lista:
                search_dict(diccionario, key_to_search, value_to_search)

        

if __name__ == "__main__":

    url = "https://api.publicapis.org/entries"
    dict_ints = {'Primitivo': 0,'Int': 0, 'String': 0, 'Float': 0, 'Tupla': 0, 'Lista': 0, 'Dict': 1}
    # Archivo de prueba
    socket.getaddrinfo('22.88.107.0', 8080)
    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    #print(response_json)
    print("===================================")

    search_value(response_json)