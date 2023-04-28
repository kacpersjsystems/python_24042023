
def get_products():
    with psycopg2.connect(host=getenv('DB_HOST'), database=getenv('DB_NAME'), user=getenv('DB_USER'),
                          password=getenv('DB_PASSWORD')) as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT 
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
    	discontinued=0;''')

    return cursor.fetchall()