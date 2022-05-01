import json
from asyncore import read
from click import command
import psycopg2
import csv
import sys
import flask


def generate_result(data):
    print("insert")
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
    )
    cursor = conn.cursor()
    print(data)
    movieName = data["movieName"]
    startYear = data["movieYear"]
    averageRating = data["rating"]
    genres = data["genres"]
    print(genres)
    tconst = generate_tconst()
    print(tconst)
    sql = "insert into movie (tconst, startYear, primaryTitle, averageRating, genres) values (%s, %s, %s, %s, %s) "
    val = (tconst, startYear, movieName, averageRating, genres)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return


def generate_tconst():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
    )
    cursor = conn.cursor()
    sql = "select max(tconst) from movie;"
    cursor.execute(sql, ())
    result = cursor.fetchall()
    result = result[0][0]
    tconst = int(result[2:])
    tconst += 1
    tconst = str(tconst)
    if len(tconst) <= 7:
        while len(tconst) != 7:
            tconst = "0" + tconst
    return "tt" + tconst
