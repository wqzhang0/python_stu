import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
#
#
from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()
def get_db():
    if 'db' not in g:
        g.db =   SQLAlchemy()

        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES
                               )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))



@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')



def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

#
# from flask_demo.flaskr import db
#
#
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password= db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.String(120), nullable=False)
    created = db.Column(db.String(120), unique=True, nullable=False)
    author_id = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)

#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
#
#     category = db.relationship('Category', backref=db.backref('posts', lazy=True))
#
#     def __repr__(self):
#         return '<Post %r>' % self.title
#
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#
#     def __repr__(self):
#         return '<Category %r>' % self.name

# db.drop_all()
# admin = User(username='admin', email='admin1@example.com')
# db.session.add(admin)
# db.session.commit()
# a = User.query.all()

# py_category = Category(name='Python')
# Post(title='Hello python', body='Python is pretty coll', category=py_category)
# p = Post(title='Snakes', body="Sssss")
# py_category.posts.append(p)
# db.session.add(py_category)
# py_category.posts



# db.session.commit()
# print(a)