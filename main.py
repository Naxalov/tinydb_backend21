from tinydb import TinyDB
db = TinyDB('db.json')
# Document

# db.truncate()
user1 = {'user_id':1,'username':'username1'}
user2 = {'user_id':2,'username':'username2'}
user3 = {'user_id':3,'username':'username3'}
user4 = {'user_id':4,'username':'username4'}
user5 = {'user_id':5,'username':'username5'}


db.insert(user1)
db.insert(user2)
db.insert(user3)
db.insert(user4)
db.insert(user5)
