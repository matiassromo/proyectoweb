from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.views.user_view import router as UserRouter

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia esto al puerto de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Permitir todas las cabeceras
)

# Servir la carpeta 'static' en la ruta '/'
app.include_router(UserRouter, tags=["Users"], prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a la API con MongoDB"}
