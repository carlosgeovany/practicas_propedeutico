
import json

#función que recibe una lista de tipo string y remueve los espacios en blanco que tenga cada elemento y regresa una lista
def strip_list(l):
    return[x.strip() for x in l]  
    
#definimos unas listas donde guardar nuestros valores
ticket = []
carrier = []
track = []
#en caso de un error al leer el archivo, cachamos el error e imprimimos un mensaje
try:
    with open("test.txt", 'r', encoding='utf8') as f:
        lines = f.readlines()[5:]
        for line in lines:
            ticket.append(line[12:23])
            carrier.append(line[181:194])
            track.append(line[194:230])
except Exception as e:
        print ('Error occurred:\n' + str(e))          

#mandamos a llamar a nuestra función
ticket = strip_list(ticket)
carrier = strip_list(carrier)
track = strip_list(track)

#unimos tres listas para crear un diccionario
dic = dict(zip(ticket, zip(carrier, track)))
print("Diccionario:")
print(dic)

#recorremos nuestro diccionario y eliminamos los elementos cuyo valor no sea 'UPS'
for key, value in dict(dic).items():
        if value[0] != 'UPS':
            del dic[key]
print("Diccionario solo UPS:")
print(dic)

#solo vamos a convertir el valor de las llaves
dic = {int(k):[i for i in v] for k,v in dic.items()}
print("El maximo valor de las llaves es: " + str(max(dic)))
print("El minimo valor de las llaves es: " + str(min(dic)))

#Debido a que no podemos escribir directamente nuestro direccionario a un archivo, antes debemos serializarlo con la ayuda de la librería json
#en caso de que no podamos hacer la escritura al archivo, mcachamos la excepción e imprimimos un mensaje
try:
    with open('UPS.txt', 'w') as f:
        f.write(json.dumps(dic))
except Exception as e:
        print ('Error occurred:\n' + str(e))   