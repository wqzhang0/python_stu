import os
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_demo.flaskr.db import db, User


def create_app(test_config=None):
    # create and configure the app
    print(__name__)
    app = Flask(__name__, instance_relative_config=True)
    app.debug = True
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/index')
    def index():
        return 'main page'

    from flask_demo.flaskr import auth
    app.register_blueprint(auth.bp)
    from flask_demo.flaskr import blog
    app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='auth.login')
    app.add_url_rule('/', endpoint='index')
    return app


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////python_stu/flask_demo/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysql.520@47.98.211.102:3306/flask'
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password= db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# class Todo(db.Model):
#     __tablename__ = 'todos'
#     id = db.Column('todo_id', db.Integer, primary_key=True)
#     title = db.Column(db.String(60))
#     text = db.Column(db.String)
#     done = db.Column(db.Boolean)
#     pub_date = db.Column(db.DateTime)
#
#     def __init__(self, title, text):
#         self.title = title
#         self.text = text
#         self.done = False
#         self.pub_date = datetime.utcnow()
#
# db.drop_all()
# db.create_all()
app.run()
