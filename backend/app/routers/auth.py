from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import jwt
import bcrypt
import asyncpg
import datetime
from config import SECRET_KEY

router = APIRouter()

async def get_db():
    return await asyncpg.connect("postgresql://myuser:mypassword@localhost:5432/codeversus")


class User(BaseModel):
    username: str
    password: str


def hash_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def verify_password(password: str, hashed_password: bytes):
    return bcrypt.checkpw(password.encode(), hashed_password)


def create_jwt(username: str):
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


@router.post("/signup")
async def signup(user: User):
    db = await get_db()

    existing_user = await db.fetchrow("SELECT * FROM users WHERE username = $1", user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    hashed_password = hash_password(user.password)

    await db.execute("INSERT INTO users (username, password) VALUES ($1, $2)", user.username, hashed_password)

    return {"message": "Пользователь зарегистрирован"}


@router.post("/login")
async def login(user: User):
    db = await get_db()

    existing_user = await db.fetchrow("SELECT * FROM users WHERE username = $1", user.username)
    if not existing_user:
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или пароль")

    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или пароль")

    token = create_jwt(user.username)

    return {"token": token}
