# -*- coding: utf-8 -*-

import psycopg2
import conf


def pg_init():
    """
    初始化数据库链接
    :return:
    """
    global connection
    connection = psycopg2.connect(database=conf.settings["database"],
                              user=conf.settings["user"],
                              password=conf.settings["password"],
                              host=conf.settings["host"],
                              port=conf.settings["port"]
                              )


def get_cursor():
    """
    生成光标
    :return:
    """
    cursor = connection.cursor()
    return cursor


def get_edu():
    """
    获取教育相关字段
    :return:
    """
    # sql_edu = "SELECT id, major, edu_intr, work_title, work_intr FROM person limit 10000;"
    sql_edu = "SELECT id, major, edu_intr, work_title, work_intr FROM person limit 5;"
    cursor = get_cursor()
    cursor.execute(sql_edu)
    raw = cursor.fetchall()
    return raw

