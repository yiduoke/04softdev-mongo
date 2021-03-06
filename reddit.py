'''
/r/DeepFried json from reddit
it includes data about each post on the front page of the DeepFried at real time if you comment stuff in

https://www.reddit.com/r/deepfried.json

I got rid of several top layers so I could have separate documents for each post
I just established a connection in this script
'''

import pymongo
import json, urllib2
from pprint import pprint

object = urllib2.urlopen("https://www.reddit.com/r/deepfried.json")
string = object.read()
d = json.loads(string)

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection['keY-taoI']
collection = db['r/deepFried']

# cleaning it up so the upper layers are gone
# for document in d['data']['children']:
#     collection.insert(document['data'])

def below_score(threshold):
    output = collection.find({"score" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_score(threshold):
    output = collection.find({"score" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def below_ups(threshold):
    output = collection.find({"ups" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_ups(threshold):
    output = collection.find({"ups" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def below_comments(threshold):
    output = collection.find({"num_comments" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_comments(threshold):
    output = collection.find({"num_comments" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def is_video(boolean):
    output = collection.find({"is_video" : boolean})
    for i in output:
   		pprint(i)

def good_video(score_threshold, ups_threshold):
    output = collection.find({"is_video" : True, "score": {'$gt': score_threshold}, "ups": {'$gt': ups_threshold}})
    for i in output:
   		pprint(i)