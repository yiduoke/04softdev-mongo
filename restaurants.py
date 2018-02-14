<<<<<<< HEAD
import pymongo;

connection = pymongo.MongoClient("homer.stuy.edu");

db = connection.test
collection = db.restaurants

# All restaurants in a specified borough.
# All restaurants in a specified zip code.
# All restaurants in a specified zip code and with a specified grade.
# All restaurants in a specified zip code with a score below a specified threshold.
# Something more clever.


def borough(x):
	print collection.find({"borough" : x})
	return collection.find({"borough" : x})

def zip(x):
	print collection.find("address" : {"zipcode" : x})
	return collection.find("address" : {"zipcode" : x})

zip("11358")


=======
import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.test
collection = db.restaurants

def borough(x):
    return db.restaurants.find({"borough": x})

def zipcode(x):
    return db.restaurants.find({"address.zipcode": str(x)})

def belowRating(zipcode, threshold):
    return db.restaurants.find({$and: [{"address.zipcode": zipcode}, {"grades.score": {$lt: threshold}} ] })

def notClever(grade, score):
    db.restaurants.find({$and: [{"grades.grade": {$gt: grade} }, {"grades.score": {$gt: score} } ] })
>>>>>>> 7147e7c8de15930f9bbff10534f612403d28bf20
