import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'solo_traveller_handbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

class User(Document):
    username = StringField(unique=True)
    email = EmailField(unique=True, required=True)
    password = BinaryField(required=True)

@app.route('/')
@app.route('/home')
def index():

    my_name= 'Nafeesah'
    return render_template("index.html", my_name=my_name)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)