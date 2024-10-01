from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.views.user_view import router as UserRouter

app = FastAPI()

# Servir la carpeta 'static' en la ruta '/'

app.include_router(UserRouter, tags=["Users"], prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a la API con MongoDB"}
