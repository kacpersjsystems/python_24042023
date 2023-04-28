from os import getenv
import psycopg2


def get_product_by_id(product_id: int):
    with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'),
                          password=getenv('DB_PASSWORD')) as connection:
        cursor = connection.cursor()
        cursor.execute(_build_query(product_id))

        return cursor.fetchone()


def get_products():
    with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'),
                          password=getenv('DB_PASSWORD')) as connection:
        cursor = connection.cursor()
        cursor.execute(_build_query())

        return cursor.fetchall()


def _build_query(product_id=None) -> str:
    sql = '''SELECT 
    	product_id,
    	product_name,
    	unit_price,
    	units_in_stock,
    	suppliers.company_name as supplier_name,
    	categories.category_name 
    FROM
    	products
    LEFT JOIN suppliers ON products.supplier_id  = suppliers.supplier_id 
    LEFT JOIN categories ON products.category_id  = categories.category_id 
    WHERE
    	discontinued=0'''

    if product_id is not None:
        sql += f' AND product_id={(int(product_id))}'

    return sql