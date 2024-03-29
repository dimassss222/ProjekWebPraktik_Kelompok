from app.model.user import Users
from flask import request
from app import response
from app.db_entri import db

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

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

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        return f"{e}"

def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    return data

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Successfully create data!')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(id=id).first()
        user.email = email
        user.name = name
        user.setPassword(password)
        db.session.commit()
        return response.ok('', 'Successfully update data!')
    except Exception as e:
        print(e)

def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty....')
        
        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)

def login():
    try:
        email = request.json['email']
        password = request.json['password']
        user = Users.query.filter_by(email = email).first()

        if not user:
            return response.badRequest([], 'Empty....')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'Your credentials is invalid')
        
        data = singleTransform(user)
        return response.ok(data, "")
    
    except Exception as e:
        print(e) 