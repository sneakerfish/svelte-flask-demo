import os, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import Schema, fields, validate, post_load
from flask_marshmallow import Marshmallow
from sqlalchemy import delete, update
from app import create_app, db
from models import TodoModel

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
CORS(app)
ma = Marshmallow(app)

todos = []


class TodoSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1))
    completed = fields.Boolean(default=False)

    @post_load
    def make_todo(self, data, **kwargs):
        return data

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = TodoModel.query.all()
    return todos_schema.dump(todos), 200

@app.route('/todos', methods=['PUT'])
def create_todo():
    todo = todo_schema.load(request.get_json())
    db_todo = TodoModel(**todo)
    db.session.add(db_todo)
    db.session.commit()
    return todo_schema.dump(todo), 201  # Created

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = db.session.get(TodoModel, int(todo_id))
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return todo_schema.dump(todo), 200

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    db_todo = TodoModel.query.filter_by(id=todo_id).first()
    if db_todo is None:
        return jsonify({'error': 'Todo not found'}), 404  # Not Found

    todo = todo_schema.load(request.get_json())

    updated = False
    if 'title' in todo:
        db_todo.title = todo['title']
        updated = True
    if 'completed' in todo:
        if todo['completed'] is None:
            db_todo.completed = None
        else:
            db_todo.completed = datetime.datetime.strptime(todo['completed'], '%Y-%m-%d %H:%M:%S')
        updated = True
    if updated:
        db.session.add(db_todo)
        db.session.commit()
    return todo_schema.dump(todo), 200  # OK

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = TodoModel.query.filter_by(id=todo_id).first()
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404  # Not Found

    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': f'Todo item with ID {todo_id} deleted'}), 200  # OK


if __name__ == '__main__':
    app.run(debug=True)
