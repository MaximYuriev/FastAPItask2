from fastapi import APIRouter, Body
from typing import Union, Annotated
from models.good import Main_User, Main_UserDB, New_Respons

users_router = APIRouter()

def coder_password(cod: str):
    result = cod*2

users_list = [Main_UserDB(name = 'Ivanov',age = 20,id = 108, password = '**********'),Main_UserDB(name = 'Petrov',age = 25,id = 134, password = '***********')]

def find_user(id: int) -> Union[Main_UserDB,None]:
    for user in users_list:
        if user.id == id:
            return user
    return None
@users_router.get("/api/users",response_model = Union[list[Main_User],None])
def get_users():
    return users_list

@users_router.get("/api/users/{id}", response_model = Union[Main_User, New_Respons])
def get_user(id: int):
    user = find_user(id)
    if user == None:
        return New_Respons(message = "Пользователь не найден")
    return user

@users_router.post("/api/users",response_model=Union[Main_User, New_Respons])
def create_user(item: Annotated[Main_User,Body(embed = True, description="Новый пользователь")]):
    user = Main_UserDB(name = item.name,age = item.age,id = item.id,password = coder_password(item.name))
    users_list.append(user)
    return user

@users_router.put("/api/users", response_model=Union[Main_User, New_Respons])
def edit_person(item: Annotated[Main_User,Body(embed = True, description="Изменение данных пользователя по id")]):
    user = find_user(item.id)
    if user == None:
        return New_Respons(message = "Пользовател не найден")
    user.id = item.id
    user.name = item.name
    user.age = item.age
    return user

@users_router.delete("/api/users/{id}",response_model=Union[list[Main_User],None])
def delete_person(id: int):
    user = find_user(id)
    if user == None:
        return New_Respons(message = "Пользователь не найден")
    users_list.remove(user)
    return users_list












































