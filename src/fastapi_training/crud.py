from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class CreateIn(BaseModel):
    name: str
    nickname: str


class CreateOut(BaseModel):
    status: str
    id: int


# Create a FastAPI instance
app = FastAPI()

# Users database
users_db = {}


@app.post("/users/", response_model=CreateOut)
async def create_user(user: CreateIn):
    user_dict = user.dict()
    user_dict.update({"status": "success", "id": len(users_db)})

    # Update db
    users_db.update({user.name: user_dict})
    return user_dict


@app.get("/name/{name}")
async def read_user(name: str):
    user = users_db.get(name)
    if not user:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        return user


@app.put("/users/", response_model=CreateOut)
async def update_user(user: CreateIn):
    new_user_dict = user.dict()
    old_user_dict = users_db.get(user.name)
    if not old_user_dict:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        new_user_dict.update({"status": "success", "id": old_user_dict["id"]})
        
        # Update db
        users_db.update({user.name: new_user_dict})
        return new_user_dict


@app.delete("/name/{name}")
async def delete_user(name: str):
    user = users_db.get(name)
    if not user:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        users_db.pop(name)
