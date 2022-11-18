from model.models import Invoice, Client, Order
from .sql import Datastore
from mysql.connector import Error


def result_to_invoice(result) -> Invoice:
    return Invoice(invoice_id=result[0], invoice_date=result[1], status=result[2],
                   discount=result[3], amount=result[4],
                   order=Order(order_id=result[5], order_placement_date=result[6],
                               order_fulfillment_date=result[7],
                               client=Client(client_id=result[8], client_name=result[9],
                                             client_phone_number=result[10],
                                             client_email=result[11], date_joined=result[12])))


class Invoices(Datastore):
    def __init__(self):
        super().__init__()

    @classmethod
    def fetch_invoices(cls) -> [Invoice]:
        conn = cls.fetch_connection()
        query = 'SELECT i.invoice_id, i.invoice_date, i.status, i.discount, i.amount, o.order_id, ' \
                'o.order_placement_date, o.order_fulfillment_date, c.client_id, c.client_name, ' \
                'c.client_phone_number, c.client_email, c.date_joined FROM invoice i INNER JOIN orders ' \
                'o ON i.order_id = o.order_id INNER JOIN client c ON o.client_id = c.client_id'
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            # conn.close()
            print('Select invoice successful')
            invoices = []
            for res in result:
                invoice = result_to_invoice(res)
                invoices.append(invoice)

            return invoices

        except Error as e:
            print(f'Error occurred while fetching invoices: {e}')

    @classmethod
    def fetch_invoice_by_id(cls, pk: int) -> Invoice | None:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'SELECT i.invoice_id, i.invoice_date, i.status, i.discount, i.amount, o.order_id, ' \
                'o.order_placement_date, o.order_fulfillment_date, c.client_id, c.client_name, ' \
                'c.client_phone_number, c.client_email, c.date_joined FROM invoice i INNER JOIN orders ' \
                'o ON i.order_id = o.order_id INNER JOIN client c ON o.client_id = c.client_id WHERE i.invoice_id = %s'
        param = (pk,)
        try:
            cursor.execute(query, param)
            result = cursor.fetchone()
            if result is None:
                return None
            invoice = result_to_invoice(result)
            return invoice
        except Error as e:
            print(f'Error fetching invoice by id: {e}')

    @classmethod
    def insert_invoice(cls, invoice: Invoice) -> int:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'INSERT INTO invoice (invoice_date, status, discount, amount, order_id) VALUES (%s, %s, %s, %s, %s)'
        params = (invoice.invoice_date, invoice.status, invoice.discount, invoice.amount, invoice.order.order_id,)
        try:
            cursor.execute(query, params)
            return cursor.lastrowid
        except Error as e:
            print(f'Error while inserting an invoice: {e}')

    @classmethod
    def delete_invoice(cls, pk: int) -> bool:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'DELETE FROM invoice WHERE invoice_id = %s;'
        params = (pk,)
        res = False
        try:
            cursor.execute(query, params)
            res = True
        except Error as e:
            print(f'An error occurred while deleting invoice: {e}')
        return res

