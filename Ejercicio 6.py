from pymongo import MongoClient

uri = ""
client = MongoClient(uri)
db = client.ejercicios

clientes = [
{ "cliente": "Alice Johnson", "productos": [ { "nombre": "Laptop", "precio": 1200.00 }, { "nombre": "Smartphone Galaxy S23", "precio": 899.99 }, { "nombre": "Audífonos Noise Cancelling Pro", "precio": 249.99 } ] },
{ "cliente": "Bob Williams", "productos": [ { "nombre": "Smart TV OLED 65 pulgadas", "precio": 1800.00 }, { "nombre": "Soundbar Dolby Atmos", "precio": 450.00 } ] },
{ "cliente": "Charlie Brown", "productos": [ { "nombre": "Tablet", "precio": 650.00 }, { "nombre": "Apple Watch Series 9", "precio": 429.00 }, { "nombre": "Teclado Mecánico RGB", "precio": 120.00 } ] },
{ "cliente": "Diana Prince", "productos": [ { "nombre": "Cámara Mirrorless 4K", "precio": 1500.00 }, { "nombre": "Lente Gran Angular", "precio": 700.00 }, { "nombre": "Gimbal Estabilizador", "precio": 300.00 } ] },
{ "cliente": "Eve Davis", "productos": [ { "nombre": "Consola de Videojuegos PlayStation 5", "precio": 499.99 }, { "nombre": "Controlador Inalámbrico Extra", "precio": 69.99 }, { "nombre": "Juego Cyberpunk 2077", "precio": 59.99 } ] },
{ "cliente": "Frank White", "productos": [ { "nombre": "Monitor Curvo Gaming 27 pulgadas", "precio": 350.00 }, { "nombre": "Mouse Gaming Profesional", "precio": 75.00 }, { "nombre": "Auriculares Gaming con Micrófono", "precio": 99.00 } ] },
{ "cliente": "Grace Taylor", "productos": [ { "nombre": "Impresora Multifuncional WiFi", "precio": 180.00 }, { "nombre": "Disco Duro Externo 2TB", "precio": 80.00 } ] },
{ "cliente": "Henry Moore", "productos": [ { "nombre": "Robot Aspirador Inteligente", "precio": 400.00 }, { "nombre": "Cámara de Seguridad IP", "precio": 90.00 } ] },
{ "cliente": "Ivy King", "productos": [ { "nombre": "Laptop", "precio": 250.00 }, { "nombre": "Pantalla de Proyección Plegable", "precio": 100.00 } ] },
{ "cliente": "Jack Lewis", "productos": [ { "nombre": "Dron con Cámara 4K", "precio": 900.00 }, { "nombre": "Batería Extra para Dron", "precio": 80.00 } ] },
{ "cliente": "Karen Hall", "productos": [ { "nombre": "Sistema de Sonido Multi-room", "precio": 700.00 }, { "nombre": "Altavoz Inteligente con Asistente", "precio": 150.00 } ] },
{ "cliente": "Liam Scott", "productos": [ { "nombre": "Router WiFi 6 de Alta Velocidad", "precio": 160.00 }, { "nombre": "Extensor de Rango WiFi", "precio": 50.00 } ] },
{ "cliente": "Mia Green", "productos": [ { "nombre": "Tablet", "precio": 130.00 }, { "nombre": "Funda Protectora para Ebook Reader", "precio": 25.00 } ] },
{ "cliente": "Noah Adams", "productos": [ { "nombre": "Cafetera Inteligente Programable", "precio": 190.00 }, { "nombre": "Freidora de Aire Digital", "precio": 120.00 } ] },
{ "cliente": "Olivia Baker", "productos": [ { "nombre": "Dron con Cámara 4K", "precio": 1300.00 }, { "nombre": "Controladores VR Move", "precio": 80.00 } ] }]


#db.ejercicio6.insert_many(clientes)

productos = db.ejercicio6.find({"productos": {"$elemMatch": {"nombre": "Dron con Cámara 4K", "precio": {"$lt": 1000}}}})

for i in productos:
    print(i)
client.close()