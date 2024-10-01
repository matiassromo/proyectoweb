# views/user_view.py
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from backend.controllers.user_controller import (
    add_user,
    retrieve_users,
    retrieve_user,
    update_user,
    delete_user
)
from backend.models.user import UserSchema, UpdateUserModel

router = APIRouter()

# Crear un nuevo usuario
@router.post("/users/", response_description="Agregar un nuevo usuario")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return new_user

# Obtener todos los usuarios
@router.get("/users/", response_description="Obtener todos los usuarios")
async def get_users():
    users = await retrieve_users()
    return users

# Obtener un usuario por ID
@router.get("/users/{id}", response_description="Obtener un usuario por ID")
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")

# Actualizar un usuario por ID
@router.put("/users/{id}", response_description="Actualizar un usuario")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return {"message": "Usuario actualizado correctamente"}
    raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")

# Eliminar un usuario por ID
@router.delete("/users/{id}", response_description="Eliminar un usuario")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")
