from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Medatabase.db'
db = SQLAlchemy(app)

class TopicModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    problem = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Topic(topic = {self.topic}, links = {self.link}, problem = {self.problem})"

# ekbar run kore felar poree ar run er dorkar nai nahole barbar create hbe
# with app.app_context():
#     db.create_all()



task_put_args = reqparse.RequestParser()
task_put_args.add_argument("topic", type=str, help="ERROR MESSAGE")
task_put_args.add_argument("link", type=str, help="ERROR MESSAGE")
task_put_args.add_argument("problem", type=str, help="ERROR MESSAGE")

# videos dictionary will store the infos

Tasks = {
    1: {"topic": "FLASK-REST", "link":"www.youtube.com", "problem":"Still did not work with Database"},
    2: {"topic": "Langchain", "link":"www.youtube.com", "problem":"Did not complete it"},
}

resource_fields = {
    'id':fields.Integer,
    'topic': fields.String,
    'link': fields.String,
    'problem': fields.String
}
# The marshal_with in 45 line will take  the syntax of 37 line resource field to get the datas from get
class Task_Learned(Resource):
    @marshal_with(resource_fields)
    def get(self, task_id):
        # Will send the specific video I ask for
        result = TopicModel.query.filter_by(id = task_id).first()
        return result
    # Creating New Task using put method
    @marshal_with(resource_fields)
    def put(self, task_id):
        # print(request.form)
        args = task_put_args.parse_args()
        tasks = TopicModel(id=task_id, name=args['topic'], link=args['link'], problem=args['problem'])
        # These are like git
        db.session.add(tasks)
        db.session.commit()
        return tasks, 201


# Asking for the specific video through this api
api.add_resource(Task_Learned, "/task/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)