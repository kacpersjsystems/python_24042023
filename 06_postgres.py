from os import getenv

from dotenv import load_dotenv
import psycopg2

from utils import parse_args
load_dotenv()

args = parse_args()


class Screen:
    def __init__(self, connection):
        self.connection = connection

    def add(self, args):
        print('Dodaje nowy')
        print(args.name, args.event_at)
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO events(name, event_at) VALUES(%s, %s)', (args.name, args.event_at))
        self.connection.commit()

    def index(self, args):
        print('Wypisuje wszystkie')
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, name, event_at FROM events ORDER BY event_at ASC')
        data = cursor.fetchall()
        for id, name, event_at in data:
            print(id, name, event_at)

    def complete(self, args):
        print('Zrobione!')
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM events WHERE id=%s', (args.id,))
        self.connection.commit()


with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'), password=getenv('DB_PASSWORD')) as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS events(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            event_at TIMESTAMP
        )''')
    connection.commit()
    print('commit')

    screen = Screen(connection)

    match args.operation:
        case 'add': screen.add(args)
        case 'index': screen.index(args)
        case 'complete': screen.complete(args)
        case _: raise ValueError('Unknown operation')