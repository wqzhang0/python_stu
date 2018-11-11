import os
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_demo.flaskr.db import db, User


def create_app(test_config=None):
    # create and configure the manager
    print(__name__)
    app = Flask(__name__, instance_relative_config=True)
    app.debug = True
    # manager.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(manager.instance_path, 'flaskr.sqlite'),
    # )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////python_stu/flask_demo/test.db'

    # manager.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(manager.instance_path, 'flaskr.sqlite')
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
    # manager.app_context().push()
    # db.create_all()
    # db.drop_all()

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
    # manager.add_url_rule('/', endpoint='auth.login')
    app.add_url_rule('/', endpoint='index')
    return app


app = create_app()
app.run()
