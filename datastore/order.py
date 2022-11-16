from model.models import Order
from .sql import Datastore
from mysql.connector import Error

class Orders(Datastore):
    def __init__(self):
        super().__inti__

    @classmethod
    def insert_order(cls, id: int, order: Order) -> int:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'INSERT INTO orders (order_placement_date, order_fulfillment_date, client_id) VALUES (%s, %s, %s)'
        params = (order.order_placement_date, order_fulfillment_date, id, )
        try:
            cursor.execute(query)
            return cursor.lastrowid
        except Error as e:
            print(f'An error occurred while inserting client: {e}')
            return 0

    @classmethod
    def update_order(cls, id: int, order: Order) -> bool:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'UPDATE orders SET order_fulfillment_date=%s'
        params = (order.order_fulfillment_date, )
        try:
            cursor.execute(query, params)
            return true
        except Error as e:
            print(f'An error occurred while updating order: {e}')
            return false

    @classmethod
    def fetch_orders(cls) -> [Order]:
        conn = cls.fetch_connection()
        query = 'SELECT o.order_id, o.order_placement_date, o.order_fulfillment_date, c.client_id, c.client_name, c.client_phone_number, c.client_email, c.date_joined FROM orders o INNER JOIN clients c ON o.client_id = c.client_id'
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            orders = []
            for order in result:
                temp_order = Order(order_id=result[0], order_placement_date=result[1], order_fulfillment_date=result[2], client=Client(client_id=result[3], client_name=result[4], client_phone_number=result[5], client_email=result[6], date_joiend=result[7]))
                orders.append(temp_order)
            except Error as e:
                print(f'Error fetching orders: {e}')
            cursor.close()
            conn.close()
            return orders

    @classmethod
    def fetch_order_by_id(cls, id: int) -> Order | None:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'SELECT o.order_id, o.order_placement_date, o.order_fulfillment_date, c.client_id, c.client_name, c.client_phone_number, c.client_email, c.date_joined FROM orders o INNER JOIN clients c ON o.client_id = c.client_id WHERE o.order_id = %s'
        params = (id, )
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is None:
                return None:
             order = Order(order_id=result[0], order_placement_date=result[1], order_fulfillment_date=result[2], client=Client(client_id=result[3], client_name=result[4], client_phone_number=result[5], client_email=result[6], date_joiend=result[7]))
             return order
         except Error as e:
             print(f'An error occurred while fetching order: {e}')
             return None

    @classmethod
    def delete_order(cls, id: int) -> bool:
        conn = cls.fetch_connection()
        cursor = conn.cursor()
        query = 'DELETE FROM orders WHERE order_id = %s'
        params = (id, )
        try:
            cursor.execute(query, params)
            return true
        except Error as e:
            print(f'Error deleting order: {e}')
            return false

