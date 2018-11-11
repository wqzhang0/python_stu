from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# manager = Flask(__name__)
#
# manager.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
# manager.debug = True
engine = create_engine("mysql+pymysql://root:Mysql.520@47.98.211.102:3306/flask", max_overflow=5)

# manager.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysql.520@47.98.211.102:3306/flask'
# db = SQLAlchemy(manager)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

# 获取元数据
metadata = MetaData()
# 定义表
user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )

# db.create_all()

# 创建数据表，如果数据表存在，则忽视
metadata.create_all(engine)
# manager.run()
engine.execute(
    "INSERT INTO color(id, name) VALUES ('1', 'liuyao');"
)