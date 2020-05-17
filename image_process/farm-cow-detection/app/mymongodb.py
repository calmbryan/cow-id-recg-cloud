import pymongo
from bson.objectid import ObjectId

class mongoConn:
    def __init__(self):
        super().__init__()
        self.client = pymongo.MongoClient("mongodb://localhost:27015/")
        self.db = self.client["test"]
        self.emptyimages = self.db["emptyimages"]
    def insertimage(self, image):
        return self.emptyimages.insert(image) #return intertedID <class 'bson.objectid.ObjectId'>
    def getall(self):
        for x in self.emptyimages.find():
            print(x)
    def query(self, post_id):
        # Convert from string to ObjectId:
        document = self.emptyimages.find_one({'_id': ObjectId(post_id)})
        return document


