from app.model.todo import Todos as Todo
from flask import request, jsonify
from app import response, db_entri
from app.controller import UserController
from app.db_entri import db


def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email,
            'password':i.password
        })
    return array

def index():
    try:
        id = request.args.get('user_id')
        todo = Todo.query.filter_by(user_id=id).all()
        data = transform(todo)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def store():
    try:
        todo = request.json['todo']
        desc = request.json['description']
        user_id = request.json['user_id']

        todo = Todo(user_id=user_id, todo=todo, description = desc)
        db.session.add(todo)
        db.session.commit()

        return response.ok('', 'Successfully create todo!')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        todo = request.json['todo']
        desc = request.json['description']

        todo = Todo.query.filter_by(id=id).first()
        todo.todo = todo
        todo.description = desc

        db.session.commit()
        return response.ok('', 'Successfully update todo!')
    
    except Exception as e:
        print(e)

# def show(id):
#     try:
#         todo = Todo.query.filter_by(id=id).first()
#         if not todo:
#             return
        
#         data = singleTransform(todo)
#         return response.ok(data, "")
    
