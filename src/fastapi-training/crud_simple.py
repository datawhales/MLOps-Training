from fastapi import FastAPI, HTTPException

# Create a FastAPI instance
app = FastAPI()

# Users database
# {name: {"name": name, "nickname": nickname}}
users_db = {}


@app.post("/name/{name}/nickname/{nickname}")
async def create_user(name: str, nickname: str):
    user = {"name": name, "nickname": nickname}
    users_db.update({name: user})
    return user


@app.get("/name/{name}")
async def read_user(name: str):
    user = users_db.get(name)
    if not user:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        return user.get("nickname")


@app.put("/name/{name}/nickname/{new_nickname}")
async def update_user(name: str, new_nickname: str):
    user = users_db.get(name)
    if not user:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        new_user = {"name": name, "nickname": new_nickname}
        users_db.update({name: new_user})
        return new_user


@app.delete("/name/{name}")
async def delete_user(name: str):
    user = users_db.get(name)
    if not user:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        users_db.pop(name)
