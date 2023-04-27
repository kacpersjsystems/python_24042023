# SQL - Structured Query Language
# Baza danych (plik)
#    Tabele (Arkusz Excela)
#      Kolumna
#
#    events
#      id
#      name
#      event_at

import sqlite3

with sqlite3.connect('events.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY,
        name TEXT,
        event_at DATETIME
    )''')
    connection.commit()
