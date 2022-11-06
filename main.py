from fastapi import FastAPI
from datastore.client import Clients

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/clients")
async def all_clients():
    clients = Clients.fetch_clients()
    return {"data": clients}
