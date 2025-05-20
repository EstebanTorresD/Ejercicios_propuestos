# Importar librerias 
from pymongo import MongoClient
import json

uri = ""

# Generar conexión mediante cliente
client = MongoClient(uri)

# Creación database empresa 
db = client.empresa

# Acceder a la colección empleados
coll = db.empleados

# Ingresamos los empleados a la base de datos
docs = [
    {"nombre": "Elena Muñoz", "departamento": {
        "nombre": "IT",
        "salario": 1200
        }
    },
    {"nombre": "Jorge Castro", "departamento": {
        "nombre": "Ventas",
        "salario": 1300
        }
    }
]

# Se insertan los documentos de empleados
result = coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")

# Mostrar empleados con salario superior a 1000 y que trabajen en 'IT'
cursor = coll.find({"$and": [{"departamento.nombre": "IT"}, {"departamento.salario": {"$gt": 1000}}]})
for cliente in cursor:
    cliente["_id"] = str(cliente["_id"])
    print(json.dumps(cliente, indent=2, ensure_ascii=False))

# Eliminamos la colección de empleados, como es la única colección dentro de 
# la base de datos, esta también es eliminada
db.empleados.drop()

#Cerrar la conexión
client.close()
