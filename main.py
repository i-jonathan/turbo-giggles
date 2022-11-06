from fastapi import FastAPI, HTTPException
from datastore.client import Clients

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/clients")
async def all_clients():
    clients = Clients.fetch_clients()
    return {"data": clients}


@app.get("/clients/{pk}")
async def fetch_client_by_id(pk):
    client = Clients.fetch_client_by_id(pk)
    if client is None:
        raise HTTPException(status_code=404, detail="Client Not Found")
    return {"data": client}
