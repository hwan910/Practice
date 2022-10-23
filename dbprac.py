from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.cecc9av.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


user = db.users.find_one({'name':'bobby'})
print(user['age'])