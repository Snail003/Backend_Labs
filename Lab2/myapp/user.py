from myapp import app
from myapp.test_data import users
from flask import request
import uuid


@app.post('/user')
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, **user_data}
    users[user_id] = user
    return user

@app.get('/user/<user_id>')
def get_user(user_id):
    return users[user_id]

@app.delete('/user/<user_id>')
def delete_user(user_id):
    deleted_user = users[user_id]
    del users[user_id]
    return deleted_user

@app.get('/users')
def get_users():
    return list(users.values())