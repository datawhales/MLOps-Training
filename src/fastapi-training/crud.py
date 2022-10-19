from fastapi import FastAPI, HTTPException

# Create a FastAPI instance
app = FastAPI()

# Items database (key: name, value: nickname)
items_db = {}

@app.post("/name/{name}/nickname/{nickname}")
async def create_item(name: str, nickname: str):
    items_db.update({name: nickname})

@app.get("/name/{name}")
async def read_item(name: str):
    nickname = items_db.get(name)
    print(nickname)
    if not nickname:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        return nickname

@app.put("/name/{name}/nickname/{new_nickname}")
async def update_item(name: str, new_nickname: str):
    nickname = items_db.get(name)
    if not nickname:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        items_db.update({name: new_nickname})

@app.delete("/name/{name}")
async def delete_item(name: str):
    nickname = items_db.get(name)
    if not nickname:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        items_db.pop(name)
