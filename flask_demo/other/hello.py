from flask import Flask, url_for, render_template, request, redirect, flash, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from flask_demo.flaskr.form_valide.RegistrationForm import RegistrationForm

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.debug = True
engine = create_engine("mysql+pymysql://root:Mysql.520@47.98.211.102:3306/flask", max_overflow=5)

# manager.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy()
db.create_all()

@app.route('/')
def index():
    flash("please login ")
    return redirect(url_for('login'))
    # return 'index'


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/auth/login", methods=['GET', 'POST'])
def login():
    def valid_login(name, pwd):
        if name == "123":
            return True

    def log_the_user_in(name):
        return render_template('hello.html', name=name)

    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalide username/password'

    return render_template('/auth/login.html', error=error)


@app.route('/search_title', methods=['GET'])
def search_title():
    key = request.args.get('key', '')
    if key == 'cangjingkong':
        return render_template('title_list.html', key=key)
    return render_template('404.html')


@app.route('/test404')
def test404():
    abort(404)


#
# string 	（缺省值） 接受任何不包含斜杠的文本
# int 	接受正整数
# float 	接受正浮点数
# path 	类似 string ，但可以包含斜杠
# uuid 	接受 UUID 字符串
# /user/<string:username>
@app.route('/user/<username>')
def prifile(username):
    return '{}\'s profile'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %s' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template("hello.html", name=name)


@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.username.data)
        print(form.email.data)
        print(form.password.data)
        flash('Thanks for registering')
        return redirect(url_for('auth/login'))
    return render_template('auth/register.html', form=form)


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


# with manager.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('prifile', username='John Doe'))
# url_for('static',filename="show_img.jpg")



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

app.config['SQLALCHEMY_BINDS'] = User


db.create_all()

app.run()
