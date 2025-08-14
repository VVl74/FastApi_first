# This is a sample Python script.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from databases import Database
import os

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class User(UserCreate):
    id: int

data_url = os.getenv("data_url", "postgresql://myuser:mypassword@192.168.100.9:5432/mydatabase")

database = Database(data_url)

@app.on_event("startup")
async def start():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def func():
    return "GOOOOOOOL"

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "Service is running"}

@app.get("/echo/{text}")
def echo(text: str):
    return {"original_text": text, "reversed": text[::-1]}

#добавление пользователя
@app.post("/users/", response_model = User)
async def create_user(user: UserCreate):
    query = "INSERT INTO users(name, email) VALUES (:name, :email) RETURNING id, name, email"
    values = {"name": user.name, "email": user.email}
    return await database.fetch_one(query=query, values=values)


# запрос списка пользователей
@app.get("/users/", response_model=list[User])
async def get_users():
    query = "SELECT id, name, email FROM users"
    return await database.fetch_all(query = query)

#запрос конкретного пользователя
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    query = "SELECT id, name, email FROM users WHERE id = :id"
    values = {"id": user_id}
    user = await database.fetch_one(query=query, values = values)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


