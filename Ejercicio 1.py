from pymongo import MongoClient

uri = ""
client = MongoClient(uri)
db = client.ejercicios

direcciones = [
{ "nombre": "Francisca Toledo", "direccion": { "ciudad": "Santiago", "calle": "Avenida Providencia 123" } },
{ "nombre": "Roberto Alarcón", "direccion": { "ciudad": "Valparaíso", "calle": "Calle Prat 456" } },
{ "nombre": "Camila Soto", "direccion": { "ciudad": "Concepción", "calle": "Avenida O'Higgins 789" } },
{ "nombre": "Andrés Sepúlveda", "direccion": { "ciudad": "Santiago", "calle": "Las Condes 001" } },
{ "nombre": "Daniela Muñoz", "direccion": { "ciudad": "Viña del Mar", "calle": "Avenida San Martín 101" } },
{ "nombre": "Jorge Vidal", "direccion": { "ciudad": "Temuco", "calle": "Avenida Alemania 202" } },
{ "nombre": "Paz Núñez", "direccion": { "ciudad": "Santiago", "calle": "Huérfanos 333" } },
{ "nombre": "Manuel Fuentes", "direccion": { "ciudad": "Antofagasta", "calle": "Balmaceda 555" } },
{ "nombre": "Lorena Reyes", "direccion": { "ciudad": "Rancagua", "calle": "Independencia 777" } },
{ "nombre": "Gonzalo Díaz", "direccion": { "ciudad": "Concepción", "calle": "Barros Arana 888" } },
{ "nombre": "Natalia Vargas", "direccion": { "ciudad": "La Serena", "calle": "Francisco de Aguirre 999" } },
{ "nombre": "Felipe Herrera", "direccion": { "ciudad": "Santiago", "calle": "Merced 111" } },
{ "nombre": "Valeria Castro", "direccion": { "ciudad": "Puerto Montt", "calle": "Benavente 222" } },
{ "nombre": "Sebastián Pinto", "direccion": { "ciudad": "Viña del Mar", "calle": "Calle Valparaíso 303" } },
{ "nombre": "Trinidad Flores", "direccion": { "ciudad": "Talca", "calle": "Uno Norte 444" } }]

#db.usuarios.insert_many(direcciones)

def busca_ciudad(city: str):
    usuarios = db.usuarios.find({"direccion.ciudad": city})
    return usuarios

usuarios = busca_ciudad("Santiago")
for i in usuarios:
    print(i)

client.close()