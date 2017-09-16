#!/usr/bin/env python
# encoding: utf-8
DEBUG = True
COOKIE_SECRET = "6aOO5ZC55LiN5pWj6ZW/5oGo77yM6Iqx5p+T5LiN6YCP5Lmh5oSB44CC"

# mongo配置
MONGO_HOST = '127.0.0.1'
MONGO_LOG_DATABASE = 'mongo_logs'

# 数据库配置
DB_HOST = '127.0.0.1'
DB_PORT = '5432'
DB_NAME = 'sxsdb'
DB_USER = 'dbuser'
DB_PASSWORD = '123kkk'

# session配置
SESSION_SECRET = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc"
STOTR_OPTIONS = {
    'redis_host': '127.0.0.1',
    'redis_port': 6379,
    'redis_pass': '123kkk',
}

try:
    from local_settings import *
except ImportError:
    pass
