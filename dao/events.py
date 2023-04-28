from datetime import datetime
from os import getenv

import psycopg2


def get_events_by_product_id(product_id: int):
    with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'),
                          password=getenv('DB_PASSWORD')) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM events WHERE product_id=%s', (product_id,))

        return cursor.fetchall()


def add_event_to_product_id(product_id: int, event_at: datetime, name: str):
    with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'),
                          password=getenv('DB_PASSWORD')) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO events(name, event_at, product_id) VALUES(%s,%s,%s)', (
            name,
            event_at.strftime('%Y-%m-%d %H:%M'),
            product_id
        ))

