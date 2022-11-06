from model.models import Client
from .sql import Datastore
from mysql.connector import Error


class Clients(Datastore):
    def __init__(self):
        super().__init__()

    @classmethod
    def fetch_clients(cls) -> [Client]:
        conn = cls.fetch_connection()
        query = 'SELECT client_id, client_name, client_phone_number, client_email, date_joined FROM client;'
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Select Clients Successful")
            clients = []
            for client in result:
                temp_client = Client(client_id=client[0], client_name=client[1],
                                     client_phone_number=client[2], client_email=client[3], date_joined=client[4])
                clients.append(temp_client)

            return clients

        except Error as e:
            print(f'Error fetching clients: {e}')

    @classmethod
    def fetch_client_by_id(cls, pk: int) -> Client | None:
        conn = cls.fetch_connection()
        query = 'SELECT client_id, client_name, client_phone_number, client_email, date_joined FROM client WHERE client_id = %s;'
        param = (pk, )
        cursor = conn.cursor()
        try:
            cursor.execute(query, param)
            result = cursor.fetchone()
            print("Select Client Successful")
            if result is None:
                return None

            client = Client(client_id=result[0], client_name=result[1],
                            client_phone_number=result[2], client_email=result[3], date_joined=result[4])
            return client
        except Error as e:
            print(f'Error fetching client with id {pk}: {e}')

    def search_by_clients_name(self, query: str) -> [Client]:
        # todo some sql to fetch clients @h4ckitt
        pass

    def insert_client(self, client: Client) -> int:
        # todo some sql to fetch clients @h4ckitt
        pass

    def update_client(self, client: Client) -> bool:
        # todo some sql to fetch clients @h4ckitt
        pass
