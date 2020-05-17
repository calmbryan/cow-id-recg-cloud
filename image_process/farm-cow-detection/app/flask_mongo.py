import os
from flask import Response, Flask
from bson.objectid import ObjectId
from mymongodb import mongoConn
import base64

app = Flask(__name__)
mydb = mongoConn() 

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<post_id>/<key>')
def get(post_id, key):
    # Convert from string to ObjectId:
    data = mydb.query(post_id)[key]
    print(len(data))
    #data = base64.b64encode(data).decode()
    resp = Response(data, mimetype="image/jpeg")
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000)