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


from flask import Flask
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

# Creting another class to get specific car. the Cars class returns all the items. Now we will get
# Only using the keys front
class Car(Resource):
    def get(self, index_or_key):
        return MehrabDatabase[index_or_key]


# Setting Path for routes and this is almost simillar as the route/api files of laravel
api.add_resource(Cars, '/')
# Another API for Car to get the specific Ids Car
api.add_resource(Car, '/<int:index_or_key>')

if __name__ == "__main__":
    app.run(debug=True)