# views/database.py
from motor.motor_asyncio import AsyncIOMotorClient

# Conectar a MongoDB en localhost:27017 (ajusta si es necesario)
MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)

# Conexión a la base de datos 'proyectoweb_db' y la colección 'users'
database = client.proyectoweb_db
user_collection = database.get_collection("users")
