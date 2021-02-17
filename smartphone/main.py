from tinydb import TinyDB

def insert_db(data_csv):

    return 0

db = TinyDB('db.json')
data = open('products.csv')
# print(products)
db.truncate()
products_db = insert_db(data)

db.insert_multiple(products_db)
