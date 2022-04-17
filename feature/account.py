from asyncore import read
from click import command
import psycopg2
import csv
import sys

def login(username,password):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
    )
    cursor = conn.cursor()
    query = "create table if not exists users (username varchar(255), password varchar(255))"
    cursor.execute(query, (username, password))
    conn.commit()
    # get actual password
    query = "Select password from Users where username=%s"
    cursor.execute(query,(username,))
    pwd = cursor.fetchall()
    print(pwd)
    if(len(pwd)==0): return "account not exists"
    actual = pwd[0][0] #[(password,)]

    # return True password matched
    if password == actual:
        return "matched"
    else: return "password doesn't match"


def register(username,password):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
    )
    cursor = conn.cursor()
    query = "create table if not exists users (username varchar(255), password varchar(255))"
    cursor.execute(query, (username, password))
    conn.commit()
    # check user is created before
    query = "Select * from Users where username=%s"
    cursor.execute(query,(username,))
    checkName = cursor.fetchall()
    # return False if created
    if (len(checkName)!=0):
        return "account exists"

    # create account with input
    query = "Insert into Users (username, password) values (%s,%s)"
    cursor.execute(query, (username,password))
    conn.commit()
    return "success"