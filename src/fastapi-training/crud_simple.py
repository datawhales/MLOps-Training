from fastapi import FastAPI, HTTPException

# Create a FastAPI instance
app = FastAPI()

# Items database
# {name: {"name": name, "nickname": nickname}}
items_db = {}


@app.post("/name/{name}/nickname/{nickname}")
async def create_item(name: str, nickname: str):
    item = {"name": name, "nickname": nickname}
    items_db.update({name: item})
    return item


@app.get("/name/{name}")
async def read_item(name: str):
    item = items_db.get(name)
    if not item:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        return item.get("nickname")


@app.put("/name/{name}/nickname/{new_nickname}")
async def update_item(name: str, new_nickname: str):
    item = items_db.get(name)
    if not item:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        new_item = {"name": name, "nickname": new_nickname}
        items_db.update({name: new_item})
        return new_item


@app.delete("/name/{name}")
async def delete_item(name: str):
    item = items_db.get(name)
    if not item:
        raise HTTPException(status_code=400, detail="Name not found")
    else:
        items_db.pop(name)
