from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

# configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MehrabDB.db'
db = SQLAlchemy(app)

# Inheriting from db.Model
class Cars(db.Model):
    # A table with id and name column
    # After writing these codes in the Task class, we will create a table through this command
    # from app import db
    # Then write this : db.create_all()
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return self.name

# Api is a part of flask_restful module

# Making a data dictionary:
MehrabDatabase = {
    1:{'name':'BMW'},
    2:{'name':'Marcedez'},
    3:{'name':'Ford'}
}
# Creating Route here :
class Cars(Resource):
    # This is almos simillar as the Controllers code in laravel
    # get request same as laravel get
    def get(self):
        return MehrabDatabase

    # Sending something now using post request
    # Eta banaisi but ekhno TEST KORI NAAII
    def post(self):
        # for sending this data we import request from flask
        data = request.json
        itemId = len(MehrabDatabase.keys()) + 1  # Selecting the index where the post requested data will be added
        MehrabDatabase[itemId] = {'name': data['name']} # Adding the new Post requested Data to the Dictionary file
        return MehrabDatabase

# Creting another class to get specific car. the Cars class returns all the items. Now we will get
# Only using the keys front
class Car(Resource):
    def get(self, index_or_key):
        return MehrabDatabase[index_or_key]


# Data for BIOS Class:
BioDatabase = {
    "Mehrab": {"Age":22, "Gender":"Male", "Study":"CSE,IIUC"},
    "Evan": {"Age":23, "Gender":"Male", "Study":"CSE,IIUC"}
}
# Creating another Class
class BIOS(Resource):
    def get(self):
        return BioDatabase

class BIO(Resource):
    def get(self, name_key):
        return BioDatabase[name_key]

# Setting Path for routes and this is almost simillar as the route/api files of laravel
api.add_resource(Cars, '/')
# Another API for Car to get the specific Ids Car
api.add_resource(Car, '/<int:index_or_key>')
# API path for Get method for BIOS:
api.add_resource(BIOS, '/BIOS')
api.add_resource(BIO, '/BIOS/<string:name_key>')



if __name__ == "__main__":
    app.run(debug=True)