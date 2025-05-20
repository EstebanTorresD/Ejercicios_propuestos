# Importar librerias 
from pymongo import MongoClient
import json

uri = ""

# Generar conexión mediante cliente
client = MongoClient(uri)

# Creación database empresa 
db = client.empresa_A

# Acceder a la colección empleados
coll = db.clientes

# Ingresamos los empleados a la base de datos
docs = [
    {"nombre": "Sofía Herrera", "empresa": "Empresa A", "facturas": [
        { "monto": 800 },
        { "monto": 1200 }
        ]
    },
    {"nombre": "Pablo Núñez", "empresa": "Empresa B", "facturas": [
        { "monto": 2000 }
        ]
    }
]

# Se insertan los documentos de los clientes
result = coll.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents.")

# Mostrar clientes de 'Empresa A' que tengan una factura mayor a $1000
cursor = coll.find({"$and": [{"empresa": "Empresa A"}, {"facturas.monto": {"$gt": 1000}}]})
for cliente in cursor:
    cliente["_id"] = str(cliente["_id"])
    print(json.dumps(cliente, indent=2, ensure_ascii=False))

# Eliminamos la colección de empleados, como es la única colección dentro de 
# la base de datos, esta también es eliminada
db.clientes.drop()

#Cerrar la conexión
client.close()