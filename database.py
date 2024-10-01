# views/database.py
from motor.motor_asyncio import AsyncIOMotorClient

# Conexión a MongoDB local (ajusta si usas MongoDB Atlas)
MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)

# Conectar a la base de datos 'proyectoweb'
database = client.proyectoweb
user_collection = database.get_collection("users")
