from pymongo import MongoClient

uri = ""
client = MongoClient(uri)
db = client.ejercicios

clientes = [
{ "nombre": "Sofía Morales", "facturas": [ { "numero": 73, "monto": 245 }, { "numero": 12, "monto": 100 } ] },
{ "nombre": "Diego Rivera", "facturas": [ { "numero": 45, "monto": 654 } ] },
{ "nombre": "Valentina Cifuentes", "facturas": [ { "numero": 91, "monto": 432 }, { "numero": 6, "monto": 450 }, { "numero": 88, "monto": 532 } ] },
{ "nombre": "Javier Guzmán", "facturas": [] },
{ "nombre": "Isidora Peña", "facturas": [ { "numero": 29, "monto": 780 } ] },
{ "nombre": "Benjamín Flores", "facturas": [ { "numero": 58, "monto": 234 }, { "numero": 7, "monto": 480 } ] },
{ "nombre": "Emilia Soto", "facturas": [ { "numero": 99, "monto": 235 } ] },
{ "nombre": "Lucas Miranda", "facturas": [ { "numero": 2, "monto": 679 }, { "numero": 81, "monto": 445 }, { "numero": 34, "monto": 125 }, { "numero": 67, "monto": 680 } ] },
{ "nombre": "Josefa Rivas", "facturas": [ { "numero": 41, "monto": 50 } ] },
{ "nombre": "Martín Aguilera", "facturas": [] },
{ "nombre": "Florencia Rojas", "facturas": [ { "numero": 100, "monto": 445 }, { "numero": 21, "monto": 890 } ] },
{ "nombre": "Sebastián Navarro", "facturas": [ { "numero": 53, "monto": 556 } ] },
{ "nombre": "Antonia Lagos", "facturas": [ { "numero": 16, "monto": 324 }, { "numero": 77, "monto": 450 } ] },
{ "nombre": "Mateo Espinoza", "facturas": [ { "numero": 64, "monto": 505 }, { "numero": 3, "monto": 448 }, { "numero": 94, "monto": 756 } ] },
{ "nombre": "Gabriela Vera", "facturas": [ { "numero": 30, "monto": 350 } ] }]

#db.ejercicio4.insert_many(clientes)

query = db.ejercicio4.find({"facturas.monto": {"$gt": 500}})

for i in query:
    print(i)

client.close()