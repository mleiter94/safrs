#!/usr/bin/env python
#
# This is a demo application to demonstrate the functionality of the safrs_rest REST API with authentication
#
# It can be ran standalone like this:
# python demo.py [Listener-IP]
#
# This will run the example on http://Listener-Ip:5000
#
# - A database is created and a item is added
# - A rest api is available
# - swagger2 documentation is generated
#
import sys
import os
import logging
import builtins
from functools import wraps
from flask import Flask, redirect, jsonify, make_response
from flask import abort, request, g, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from safrs import SAFRSBase, SAFRSJSONEncoder, Api, jsonapi_rpc
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
db  = SQLAlchemy()
auth = HTTPBasicAuth()

# Example sqla database object
class Item(SAFRSBase, db.Model):
    '''
        description: Item description
    '''

    __tablename__ = 'items'
    id = Column(String, primary_key=True)
    name = Column(String, default = '')


class User(SAFRSBase, db.Model):
    '''
        description: User description
    '''    
    __tablename__ = 'users'
    id = db.Column(String, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))
    custom_decorators = [jwt_required]

def start_app(app):

    api  = Api(app, api_spec_url = '/api/swagger', host = '{}:{}'.format(HOST,PORT), schemes = [ "http" ] )
    
    item = Item(name='test',email='em@il')
    user = User(username='admin')

    api.expose_object(Item)
    api.expose_object(User)


    # Set the JSON encoder used for object to json marshalling
    app.json_encoder = SAFRSJSONEncoder
    # Register the API at /api/docs
    swaggerui_blueprint = get_swaggerui_blueprint('/api', '/api/swagger.json')
    app.register_blueprint(swaggerui_blueprint, url_prefix='/api')

    print('Starting API: http://{}:{}/api'.format(HOST,PORT))
    app.run(host=HOST, port = PORT)


#
# APP Initialization
#

app = Flask('demo_app')
jwt = JWTManager(app)
app.config.update( SQLALCHEMY_DATABASE_URI = 'sqlite://',
                   SQLALCHEMY_TRACK_MODIFICATIONS = False,   
                   SECRET_KEY = b'sdqfjqsdfqizroqnxwc',
                   JWT_SECRET_KEY = 'ik,ncbxh',
                   DEBUG = True)
HOST = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0'
PORT = 5000
db.init_app(app)


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/')
def goto_api():
    return redirect('/api')

@app.teardown_appcontext
def shutdown_session(exception=None):
    '''cfr. http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/'''
    db.session.remove()


# Start the application
with app.app_context():
    db.create_all()
    start_app(app)
