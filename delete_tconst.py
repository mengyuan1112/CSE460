import json
from asyncore import read
from click import command
import psycopg2
import csv
import sys
import flask




def delete(tconst):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
    )
    cursor = conn.cursor()
    sql = "delete from movie where tconst = %s"
    val = (tconst,)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return