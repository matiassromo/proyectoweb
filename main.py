# main.py
from fastapi import FastAPI
from views.user_view import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["Users"], prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a la API con MongoDB"}
