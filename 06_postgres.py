from os import getenv

from dotenv import load_dotenv
import psycopg2

from utils import parse_args
load_dotenv()

args = parse_args()


with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'), password=getenv('DB_PASSWORD')) as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS events(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            event_at TIMESTAMP
        )''')
    connection.commit()
    print('commit')