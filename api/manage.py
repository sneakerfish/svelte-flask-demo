import os, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse, abort
from sqlalchemy import delete, update
from app import create_app, db
from models import TodoModel

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title is required')

todos = []


class TodoResource(Resource):
    def get(self):
        todos = TodoModel.query.all()
        json_todos = [{"id": i.id, "title": i.title, "completed": i.completed.strftime('%Y-%m-%d %H:%M:%S') if i.completed else None} for i in todos]
        return json_todos, 200

    def post(self):
        args = parser.parse_args()
        new_todo = TodoModel(title=args['title'])
        db.session.add(new_todo)
        db.session.commit()
        return {"id": new_todo.id, "title": new_todo.title, "completed": new_todo.completed.strftime('%Y-%m-%d %H:%M:%S') if new_todo.completed else None}, 201

    def put(self, id):
        args = parser.parse_args()
        todo = TodoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        todo.title = args['title']
        db.session.add(todo)
        db.session.commit()
        return {"id": todo.id, "title": todo.title, "completed": todo.completed.strftime('%Y-%m-%d %H:%M:%S') if todo.completed else None}, 200


api.add_resource(TodoResource, '/todos')

if __name__ == '__main__':
    app.run(debug=True)
