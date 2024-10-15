import os
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from backend.views.user_view import router as user_router

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://proyectoweb-bmeqh6ftezb4cwh2.canadacentral-01.azurewebsites.net"],  # Puedes poner "*" durante pruebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Login token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rutas de autenticación
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin@gmail.com" or form_data.password != "admin123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"user": "me"}

# Incluye las rutas para los usuarios
app.include_router(user_router, prefix="/api")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Puerto que Azure asigna automáticamente
    uvicorn.run(app, host="0.0.0.0", port=port)
