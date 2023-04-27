from os import getenv
from dotenv import load_dotenv
import psycopg2

load_dotenv()

with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'), password=getenv('DB_PASSWORD')) as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders LIMIT 10')

    for row in cursor.fetchall():
        print(row)


    # 14:32- 14:43