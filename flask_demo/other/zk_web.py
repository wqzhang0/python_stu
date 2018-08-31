from threading import Condition

from flask import Flask, url_for
from kazoo.client import KazooClient

from zk.zk_wrapper import zkWatch

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route("/hello_world")
def hello_world():
    # condition.acquire()
    # condition.notifyAll()
    # condition.release()

    return "Hello world!"


def proce(condition):
    condition.acquire()
    condition.notifyAll()
    condition.release()


@app.route("/login", methods=['GET', 'POST'])
def login():
    condition = Condition()

    condition.acquire()
    zkWatch(zk, "/ROOM2", proce, condition)
    condition.wait()
    condition.release()
    return "login"



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


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('prifile', username='John Doe'))

if __name__ == '__main__':
    # condition = Condition()
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    app.run()
