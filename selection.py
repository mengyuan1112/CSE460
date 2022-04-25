import json
from asyncore import read
from click import command
import psycopg2
import csv
import sys
import flask

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cursor = conn.cursor()

def generate_result(data):
    print(data)
    movieName = data["movieName"]
    startYear = data["movieYear"]
    averageRating = data["rating"]
    genres = data["genres"]
    print(genres)
    sql = "select tconst, startYear, primaryTitle, runtimeMinutes, averageRating, numVotes, isAdult, genres from movie "
    where = "where "
    val = ()
    if movieName is not None:
        where += "primaryTitle = %s and "
        val += (movieName,)
    if startYear is not None:
        where += "startYear = %s and "
        val += (startYear,)
    if averageRating is not None:
        where += "averageRating = %s and "
        val += (averageRating,)
    if genres is not None:
        where += "genres = %s;"
        val += (genres,)
    if genres is None:
        print("where")
        where = where[:-4]
        print(where)
    sql += where
    print(sql)
    print(val)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    print(result)
    return_list = []
    for i in result:
        i = list(i)
        for j in range(0, len(i)):
            i[j] =  str(i[j]) + ", "
        a = list(i)
        return_list.append(a)
    return return_list
    pass
