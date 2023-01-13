from pymongo import MongoClient

MongoClient()
client = MongoClient("mongodb+srv://ssunanda02:pass123@cluster0.jl1jke6.mongodb.net/?retryWrites=true&w=majority")
db = client.mul_prac
collection = db["mulnutrition_app"]