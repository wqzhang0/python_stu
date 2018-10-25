from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flask_demo.flaskr.auth import login_required
from flask_demo.flaskr.db import Post, User, db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts= Post.query.all()
    return render_template('blog/index.html', posts=posts)

@bp.route("/create",methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            post = Post(title=title,body=body)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
    return  render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
