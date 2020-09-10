import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dictionary'
app.config["MONGO_URI"] = 'mongodb+srv://nita:Bineta1994@myclustername.le6rk.mongodb.net/dictionary?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def words():
    return render_template("words.html", words=mongo.db.words.find())

@app.route('/add_word')
def add_word():
    return render_template('addword.html')

@app.route('/insert_task', methods=['POST'])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for('words'))

@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word =  mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_words =  mongo.db.words.find()
    return render_template('editword.html', word=the_word,
                           all_words=all_words)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)