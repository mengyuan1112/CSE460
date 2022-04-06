from asyncore import read
from click import command
import psycopg2
import csv
import sys

def login(username,password):
    conn = psycopg2.connect(
        host="localhost",
        database="cse460",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()

    # get actual password
    query = "Select password from Users where username=%s"
    cursor.execute(query,(username,))
    conn.commit()
    survey = cursor.fetchall()
    actual = survey[0][0]

    # return True password matched
    if password == actual:
        return True
    else: return False


def register(username,password):
    conn = psycopg2.connect(
        host="localhost",
        database="cse460",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()

    # check user is created before
    query = "Select * from Users where username=%s"
    cursor.execute(query,(username,))
    conn.commit()
    checkName = cursor.fetchall()
    # return False if created
    if (len(checkName)!=0):
        return False

    # create account with input
    query = "Insert into Users (username, password) values (%s,%s)"
    cursor.execute(query, (username,password))
    conn.commit()
    return True