import os
from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import delete, update
from app import create_app, db
from models import TodoModel

print("SQLALCHEMY_DATABASE_URI: ", os.getenv('SQLALCHEMY_DATABASE_URI'))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
CORS(app)
api = Api(app)




def abort_if_todo_doesnt_exist(todo_id):
    todo = TodoModel.query.get(todo_id)
    if not todo:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TodoModel.query.get(todo_id)

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        delete(TodoModel).where(TodoModel.id == todo_id)
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'title': args['title']}
        update(TodoModel).where(TodoModel.id == todo_id).values(task)
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return [i.json_dump() for i in TodoModel.query.all()]

    def post(self):
        args = parser.parse_args()
        todo = TodoModel(title=args['title'])
        db.session.add(todo)
        db.session.commit()
        return todo.json_dump(), 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)