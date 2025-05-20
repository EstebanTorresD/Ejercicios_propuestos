#importar librerias 
from pymongo import MongoClient
import json

#esta uri es propia de su cluster de mongo db
uri = ""

#generar conexión mediante cliente
client = MongoClient(uri)

#acceder a base de datos "tienda"
db = client.tienda

#acceder a la colección libros
coll = db.ordenes

#Creación de datos para la colección
docs = [
    {"cliente": "Luis Rojas", "productos": [
        {"nombre": "Teclado", "precio": 25 },
        {"nombre": "Monitor", "precio": 200 }
        ]
    },
    {"cliente": "Carla Méndez", "productos": [
        {"nombre": "Mouse", "precio": 15 },
        {"nombre": "Impresora", "precio": 120 }
        ]
    }
]

#Crear e Ingresar Datos
result = coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")

# Mostrar ordenes con un nombre especifico
cursor = coll.find({"productos.nombre": "Impresora"})
for cliente in cursor:
    cliente["_id"] = str(cliente["_id"])
    print(json.dumps(cliente, indent=2, ensure_ascii=False))

# Eliminamos la colección de empleados, como es la única colección dentro de 
# la base de datos, esta también es eliminada
db.ordenes.drop()

#Cerrar la conexión
client.close()