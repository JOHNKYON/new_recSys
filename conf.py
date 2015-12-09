# -*- coding: utf-8 -*-

from __future__ import absolute_import

import psycopg2

# 数据库连接设置
settings = {
    "database": "mydb",
    "user": "postgres",
    "password": "precure",
    "host": "127.0.0.1",
    "port": "5432"
}

# 数据库字段名
column_name = ("id", "major", "edu_intr", "work_title", "worl_intr")
