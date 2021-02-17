from tinydb import TinyDB

db = TinyDB('db.json')
products = open('products.csv').read().split('\n')
# print(products)
db.truncate()
products_db = []
for row in products[1:]:
    cat,company=row.split(',')[1:]
    products_db.append({'category':cat,'company':company})
    
# print(products_db)
# db.insert({'category':'smartphone','company':'Samsung'})
db.insert_multiple(products_db)
