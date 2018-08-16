# 配置非常简单，只需要设置 Redis 数据库的位置:\
# BROKER_URL = 'redis://localhost:6379/0'
# URL 的格式为:
# redis://:password@hostname:port/db_number
# 如果你也想在 Redis 中存储任务的状态和返回值，你应该配置这些选项:
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
from celery import Celery

app = Celery('tasks', backend  ='redis://localhost:6379/1', broker="redis://localhost:6379/0")
# app = Celery('tasks', broker="redis://localhost:6379/0")


@app.task
def add(x, y):
    print(x, y)
    return x + y
