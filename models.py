"""model for flask app

Returns:
    list: posts
"""
import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))


def create_post(name, content):
    """executes sql statement for input post

    Args:
        name (str): name of the person
        content (str): input content
    """
    con = sql.connect(path.join(ROOT, "database.db"))
    cur = con.cursor()
    cur.execute("insert into posts (name, content) values(?, ?)", (name, content))
    con.commit()
    con.close()


def get_posts():
    """fetches and returns all posts

    Returns:
        list: posts
    """
    con = sql.connect(path.join(ROOT, "database.db"))
    cur = con.cursor()
    cur.execute("select * from posts")
    posts = cur.fetchall()
    return posts
