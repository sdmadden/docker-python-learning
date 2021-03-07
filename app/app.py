import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from db import db
from models.user import User

from controllers.user import UserController

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.sep, 'app', 'settings', 'default_settings.cfg'))
app.config.from_pyfile(os.path.join(os.sep, 'app', 'settings', 'environment_settings.cfg'), silent=True)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/api/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_user(id):
    if request.method == 'PUT':
        data = request.get_json()
        try:
            UserController().update_user(id=data['id'], name=data['name'], fruit=data['fruit'])
            return "Success", 200
        except:
            return "Bad request", 400
    elif request.method == 'GET':
        return UserController().get_user(id).toJson()
    elif request.method == 'DELETE':
        pass
    else:
        return "Bad request", 400

@app.route('/api/users', methods=['POST', 'GET'])
def api_users():
    if request.method == 'POST':
        return "Not implemented", 500
    elif request.method == 'GET':
        users = UserController().get_all_users()
        return jsonify([user.toJson() for user in users])
    else:
        return "Bad request", 400

@app.route('/users/<int:id>', methods=['GET'])
def user(id):
    user = UserController().get_user(id)
    return render_template('users.html', users=[user])

@app.route('/users', methods=['GET'])
def users():
    users = UserController().get_all_users()
    return render_template('users.html', users=users)
