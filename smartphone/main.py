from tinydb import TinyDB

db = TinyDB('db.json')
products = open('products.csv').read().split('\n')
# print(products)
db.truncate()
products_db = []
for row in products[1:]:
    cat,company=row.split(',')[1:]
    db.insert({'category':cat,'company':company})
    

# db.insert({'category':'smartphone','company':'Samsung'})

