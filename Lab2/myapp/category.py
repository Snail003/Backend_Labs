from myapp import app
from myapp.test_data import categories
from flask import request
import uuid


@app.post('/category')
def create_category():
    category_data = request.get_json(silent=True)

    if category_data is None:
        return {
            "error": "No valid JSON data received"
            }, 400
    
    if "name" not in category_data:
        return {
            "error": "No name in JSON data"
            }, 400

    if not category_data["name"]:
        return {
            "error": "Empty name in JSON data"
            }, 400

    category_id = uuid.uuid4().hex
    category = {"id": category_id, "name": category_data["name"]}
    categories[category_id] = category
    return category, 201

@app.get('/category')
def get_category():
    if not request.args:
        return list(categories.values())

    category_id = request.args.get("id")
    
    if not category_id.strip():
        return list(categories.values())
    
    if category_id not in categories:
        return {
            "error": "Category could not be found"
            }, 404
    
    return categories[category_id]

@app.delete('/category')
def delete_category():
    if not request.args:
        return {
            "error": "id argument isn't found"
            }, 404
    
    category_id = request.args.get("id")
    if category_id not in categories:
        return {
            "error": "Category could not be found"
            }, 404
    
    deleted_category = categories[category_id]
    del categories[category_id]
    return deleted_category