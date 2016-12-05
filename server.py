from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask("mywebsite", template_folder=".")

database_client = MongoClient("mongodb://DBuser:password123@ds139327.mlab.com:39327/hackbudemo")

database = database_client.hackbudemo
collection = database.mark_collection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saveitem', methods=["GET"])
def saveitem():
    print(request.form)
    item = request.args["item"]
    item_object = {"item": item}
    collection.insert_one(item_object)
    return "item '%s' inserted!" % item

app.run(host="0.0.0.0", debug=True)
