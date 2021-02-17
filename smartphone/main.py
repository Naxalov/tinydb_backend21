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

table1 = db.table('products')
table2 = db.table('specifications')

data1 = open('products.csv').read()
data2 = open('specifications.csv').read()
# print(products)
db.truncate()
table1.insert_multiple( insert_db(data1))
table2.insert_multiple( insert_db(data2))



