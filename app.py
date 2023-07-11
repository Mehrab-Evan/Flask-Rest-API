# from flask import Flask, redirect, url_for, render_template
# # render_templage grabs html from render page
# # Folder names must be template
#
# app = Flask(__name__)
# @app.route("/")  # Default first Page
# def home():
#     return render_template("index.html")
#     We can return direct html in return "<>"
#
# if __name__ == "__main__":
#     app.run()

# ------------------------------------------------------


from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
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