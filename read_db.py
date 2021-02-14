from tinydb import TinyDB,Query
db = TinyDB('db.json')
# Document
# db.truncate()

q = Query()
db.remove(q.user_id==4)

data = db.all()
# user = db.search(q.user_id>2)
# print(user)

for i in data:
    print(i['user_id'])
    print(i['username'])