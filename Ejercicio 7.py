from pymongo import MongoClient

uri = ""
client = MongoClient(uri)
db = client.ejercicios

#Mostrar solo los nombres de productos de una orden.
resultado = db.ejercicio6.find()
for cliente in resultado:
    for producto in cliente['productos']:
        print(f"- {producto['nombre']}")
    print("-----------------------------------------")