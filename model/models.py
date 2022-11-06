from pydantic import BaseModel, EmailStr
from datetime import datetime
from decimal import Decimal


class Client(BaseModel):
    client_id: int
    client_name: str
    client_phone_number: str
    client_email: EmailStr
    date_joined: datetime


class Deliverable(BaseModel):
    deliverable_id: int
    deliverable_name: str
    deliverable_description: str
    base_price: Decimal


class Order(BaseModel):
    order_id: int
    order_placement_date: datetime
    order_fulfillment_date: datetime
    client: Client


class OrderLine(BaseModel):
    order_line_id: int
    quantity: int
    specification: str
    price: Decimal
    order: Order
    deliverable: Deliverable


class Invoice(BaseModel):
    invoice_id: int
    invoice_date: datetime
    status: bool
    discount: Decimal
    amount: Decimal
    order: Order


class Payment(BaseModel):
    payment_id: int
    payment_date: datetime
    payment_amount: Decimal
    payment_type: str
    invoice: Invoice
