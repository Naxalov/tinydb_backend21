from tinydb import TinyDB
db = TinyDB('db.json')
# Document
user1 = {'user_id':1,'username':'username1'}
user2 = {'user_id':2,'username':'username3'}
user3 = {'user_id':3,'username':'username6'}

# db.insert(user1)
# db.insert(user2)
# db.insert(user3)

db.insert_multiple([user1,user2])