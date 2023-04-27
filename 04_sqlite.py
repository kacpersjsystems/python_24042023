# SQL - Structured Query Language
# Baza danych (plik)
#    Tabele (Arkusz Excela)
#      Kolumna
#
#    events
#      id
#      name
#      event_at

import argparse
import sqlite3


class Screen:
    def __init__(self, connection):
        self.connection = connection

    def add(self, args):
        print('Dodaje nowy')
        print(args)

    def index(self, args):
        print('Wypisuje wszystkie')
        print(args)

    def complete(self, args):
        print('Zrobione!')
        print(args)


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--operation', required=True)
    args.add_argument('--name')
    args.add_argument('--event_at')
    args.add_argument('--id')
    return args.parse_args()


args = parse_args()

with sqlite3.connect('events.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        event_at DATETIME
    )''')
    connection.commit()

    screen = Screen(connection)

    match args.operation:
        case 'add': screen.add(args)
        case 'index': screen.index(args)
        case 'complete': screen.complete(args)
        case _: raise ValueError('Unknown operation')


# python 04_sqlite.py --operation add --name Wyjazd --event_at 2023-04-28
# INSERT INTO events(name, event_at) VALUES('Wyjazd', '2023-04-28')

# python 04_sqlite.py --operation index
# SELECT id, name, event_at FROM events ORDER BY event_at ASC

# python 04_sqlite.py --operation complete --id 1
# DELETE FROM events WHERE id=1
