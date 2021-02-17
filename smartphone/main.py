from tinydb import TinyDB

def insert_db(data_csv:str)->list:
    products = data_csv.split('\n')
    # print(products)
    collection = []
    doc_key = products[0].split(',')[1:]
    for row in products[1:]:
        doc_ = {}
        for i,x in enumerate(row.split(',')[1:]):
            doc_[doc_key[i]] = x
        collection.append(doc_)


    return collection

db = TinyDB('db.json')
# data = open('products.csv').read()
data = open('specifications.csv').read()
# print(products)
db.truncate()
products_db = insert_db(data)
db.insert_multiple(products_db)
