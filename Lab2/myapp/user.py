from myapp import app
from myapp.test_data import users
from flask import request
import uuid


@app.post('/user')
def create_user():
    user_data = request.get_json(silent=True)

    if user_data is None:
        return {
            "error": "No valid JSON data received"
            }, 400
    
    if "username" not in user_data:
        return {
            "error": "No username in JSON data"
            }, 400

    if not user_data["username"]:
        return {
            "error": "Empty username in JSON data"
            }, 400

    user_id = uuid.uuid4().hex
    user = {"id": user_id, "username": user_data["username"]}
    users[user_id] = user
    return user, 201

@app.get('/user/<user_id>')
def get_user(user_id):
    if user_id not in users:
        return {
            "error": "User could not be found"
            }, 404
    
    return users[user_id]

@app.delete('/user/<user_id>')
def delete_user(user_id):
    if user_id not in users:
        return {
            "error": "User could not be found"
            }, 404
    
    deleted_user = users[user_id]
    del users[user_id]
    return deleted_user

@app.get('/users')
def get_users():
    return list(users.values())