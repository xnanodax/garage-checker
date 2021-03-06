import pymongo
import datetime
from pytz import timezone
import pytz

client = pymongo.MongoClient()

DB_NAME = 'garagechecker'
DB_HOST = 'ds229690.mlab.com'
DB_PORT = 29690
DB_USER = 'user' #done
DB_PASS = 'user' #done

connection = pymongo.MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

collection = db.records
collection.create_index('date')

# time posted in is PST
post = {
    "status": "True",
    "created_at": datetime.datetime.now().astimezone(timezone('US/Pacific')),
}

# insert entry into db
# post_id = collection.insert_one(post).inserted_id
# print(post_id)

# read entry from db
last_entry = collection.find_one(sort=[('date', pymongo.DESCENDING)])
print(last_entry)