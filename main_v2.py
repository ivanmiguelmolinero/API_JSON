import requests
import socket

def is_primitive(data):
    return isinstance(data, int) or isinstance(data, str) or isinstance(data, float)

# Recorre el mapa y cuenta el número de dicts anidados
def read_dict(data_dict, dict_ints, f):
    #print("ENTRAMOS EN UN DICCIONARIO")
    for key in data_dict:
        #f.write((key + '\n'))
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

# Busca si hay un dict dentro de otro dict
def hay_dict(diccionario):
    encontrado = False
    for key in diccionario:
        if isinstance(diccionario[key], dict):
            encontrado = True
    return encontrado

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

def search_key(data_dict):
    for key in data_dict:
        print(key)
    key_to_search = input('Introduce alguna de estas keys para saber su valor o pulsa INTRO\n' +
                'para buscar las claves dentro de otro dict (si lo hay): ')
    if key_to_search == '':
        if hay_dict(data_dict):
            print("Ya veremos lo que se hace")
        elif hay_lista(data_dict):
            # Pintamos los 'nombres' de cada lista
            print('Los valores de las siguientes keys son listas:')
            for key in data_dict:
                if isinstance(data_dict[key], list):
                    print(key)
            key_to_search = input('Introduce la key de la lista en la que\n' +
                                  'quieres buscar más dicts: ')
            # Ahora buscamos si en esa lista hay más dicts
            if hay_dict_en_list(data_dict[key_to_search]):
                # Si los hay vamos pintando todas sus keys
                for element in data_dict[key_to_search]:
                    for key in element:
                        print(key)
                    print("DICCIONARIO TERMINADO")
                    # Ahora damos a elegir si mostrar el value de alguna key
                    # o pasar al siguiente dict
        else:
            print("No lo hay")
    else:
        print('Su valor es: ' + str(data_dict[key_to_search]))

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
    