from fastapi import FastAPI, HTTPException, Body
from datastore.client import Clients
from datastore.order import Orders
from datastore.invoice import Invoices
from model.models import Order
from model.models import Client
from model.models import Invoice

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

@app.get("/orders/{id}")
async def fetch_order_by_id(id):
    order = Orders.fetch_order_by_id(id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order Not Found")
    return {"data": order}

@app.get("/orders")
async def fetch_orders():
    orders = Orders.fetch_orders()
    return {"data": orders}

@app.get('/invoices/{id}')
async def fetch_invoice_by_order_id(id):
    invoice = Invoices.fetch_invoice_by_id(id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice Not Found")
    return {"data": invoice}

@app.get("/invoices")
async def fetch_invoices():
    invoices = Invoices.fetch_invoices()
    return {"data": invoices}

@app.post("/order/{id}/invoice")
async def generate_order_invoice(payload: dict = Body(...), id):
    invoice = Invoice(invoice_date=payload[invoice_date], status=payload[status], discount=payload[discount], amount=payload[amount], order_id=id)
    insert_id=Invoices.insert_invoice(invoice)
    return {"data": insert_id}


@app.post("/clients/{id}/orders")
async def create_order(payload: dict = Body(...)):
    order = Order(order_placement_date=payload[order_placement_date], order_fulfillment_date=payload[order_fulfillment_date])
    insert_id = Orders.insert_order(id, order)
    return {"data": insert_id}

@app.post("/client")
async def create_client(payload: dict = Body(...)):
    client = Client(client_name=payload[client_name], client_phone_number=payload[client_phone_number], client_email=payload[client_email])
    insert_id = Clients.insert_client(client)
    return {"data": insert_id}

@app.update("/orders/{id}")
async def update_order(payload: dict = Body(...), id):
    order = Order(order_fulfillment_date=payload[order_fulfillment_date])
    if Orders.update_order(id, order):
        return {"data": "order updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/client/{id}")
async def delete_client(id):
    if Clients.delete_client(id):
        return {"data": "client deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.delete("/order/{id}")
async def delete_order(id):
    if Orders.delete_order(id):
        return {"data": "order deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/invoice/{id}")
async def delete_invoice(id):
    if Invoices.delete_invoice(id):
        return {"data": "Invoice deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")

