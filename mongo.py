import pymongo
client = pymongo.MongoClient("mongodb+srv://Divyankyadav:Divyank123@divy.agggk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "divy" : "mohan",
    "radhika" : "naughty",
    "mom" : "angry"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)