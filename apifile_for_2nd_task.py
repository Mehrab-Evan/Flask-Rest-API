from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


task_put_args = reqparse.RequestParser()
task_put_args.add_argument("topic", type=str, help="ERROR MESSAGE")
task_put_args.add_argument("link", type=str, help="ERROR MESSAGE")
task_put_args.add_argument("problem", type=str, help="ERROR MESSAGE")

# videos dictionary will store the infos
videos = {}

Tasks = {
    1: {"topic": "FLASK-REST", "link":"www.youtube.com", "problem":"Still did not work with Database"},
    2: {"topic": "Langchain", "link":"www.youtube.com", "problem":"Did not complete it"},
}
class Task_Learned(Resource):
    def get(self, task_id):
        # Will send the specific video I ask for
        return Tasks[task_id]
    # Creating New Task using put method
    def put(self, task_id):
        # print(request.form)
        args = task_put_args.parse_args()
        return {task_id: args}

# Asking for the specific video through this api
api.add_resource(Task_Learned, "/task/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)