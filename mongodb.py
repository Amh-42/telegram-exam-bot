import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
ExamCollection = mydb["Exam"]
AnswerCollection = mydb["Answer"]
