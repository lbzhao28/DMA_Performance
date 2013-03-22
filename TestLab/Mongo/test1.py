__author__ = 'stone'

import pymongo
connection = pymongo.Connection('localhost',27017)

db = connection.test_database

collection = db.test_collection

import datetime
post = {"author":"Stone",
        "date":datetime.datetime.utcnow()}

posts = db.posts
posts.insert(post)

#for post in posts.find():
#    print posts.find_one()
print posts.count()
