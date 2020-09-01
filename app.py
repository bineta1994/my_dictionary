import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dictionary'
app.config["MONGO_URI"] = 'mongodb+srv://nita:Bineta1994@myclustername.le6rk.mongodb.net/dictionary?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def word():
    return render_template("words.html", words=mongo.db.words.find())

@app.route('/add')
def add():
    return "hello there"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)