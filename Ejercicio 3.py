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
    {"nombre": "Valentina Campos", "historial": [
        {"cargo": "Asistente", "año": 2018 },
        {"cargo": "Gerente", "año": 2021 }
        ]
    },
    {"nombre": "David Soto", "historial": [
        {"cargo": "Técnico", "año": 2019 },
        {"cargo": "Supervisor", "año": 2022 }
        ]
    }
]

# Se insertan los documentos de empleados
result = coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")

# Mostrar empleados con cargo "gerente" en su historial laboral
cursor = coll.find({"historial.cargo": "Gerente"})
for cliente in cursor:
    cliente["_id"] = str(cliente["_id"])
    print(json.dumps(cliente, indent=2, ensure_ascii=False))

# Eliminamos la colección de empleados, como es la única colección dentro de 
# la base de datos, esta también es eliminada
db.empleados.drop()

#Cerrar la conexión
client.close()
