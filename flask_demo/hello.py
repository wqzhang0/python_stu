from flask import Flask, url_for, render_template, request, redirect, get_flashed_messages, flash

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    flash("You were successfully logged in")
    return redirect(url_for('login'))
    # return 'index'


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/login", methods=['GET', 'POST'])
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

    return render_template('login.html', error=error)


@app.route('/search_title', methods=['GET'])
def search_title():
    key = request.args.get('key', '')
    if key == 'cangjingkong':
        return render_template('title_list.html', key=key)
    return render_template('404.html')


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


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('prifile', username='John Doe'))
# url_for('static',filename="show_img.jpg")

if __name__ == '__main__':
    # condition = Condition()
    app.debug = True
    app.run()
