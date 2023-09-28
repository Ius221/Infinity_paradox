#Creating database connection

import pymongo

url = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.1'

client = pymongo.MongoClient(url)	#Client connection

db = client['test']		#Database connection 1
db1 = client['test']	#Database connection 2

admin_collec = db['hotel_admin']	#staff collection
customer_collec = db1['hotel_customer']	#customer collection