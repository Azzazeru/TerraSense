import serial
import time
import pymongo
from datetime import datetime

from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://Aaron:1234567890@cluster0.fsizvua.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(MONGO_URI)

db = client['TerraSenseDB']
collection = db['TerraSenseApp_registro_humedad']

arduino = serial.Serial('COM8', 9600)
time.sleep(2)

dataInt = 0

while True:
    data = arduino.readline().decode('utf-8').strip()
    data1 = ''.join(filter(str.isdigit, data))
    data2 = int(data1)

    prc_humedad = data2  # Asumiendo que los datos leídos son enteros (porcentaje de humedad)
    # Crear el documento a insertar en la base de datos
    nuevo_registro = {
        'idHumedad': collection.count_documents({}) + 1,  # Obtener el nuevo ID basado en el número actual de documentos
        'prc_humedad': prc_humedad,
        'fecha_obtencion': datetime.now()
    }
    # Insertar el nuevo registro en la base de datos
    result = collection.insert_one(nuevo_registro)
    print(f"Datos insertados con el ID: {result.inserted_id}")
    time.sleep(10)  # Esperar 5 segundos antes de la siguiente inserción
