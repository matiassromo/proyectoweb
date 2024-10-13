from motor.motor_asyncio import AsyncIOMotorClient

# URI de conexión a MongoDB Atlas
client = AsyncIOMotorClient("mongodb+srv://admin:rpnBquzUeA2E75Cf@clusterprueba.vazwlz6.mongodb.net/proyectoweb?retryWrites=true&w=majority")
db = client.get_database("proyectoweb")
user_collection = db["users"]  # Aquí defines 'user_collection'
