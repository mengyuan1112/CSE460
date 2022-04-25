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
    # 可能是null，不可能是空
    # 组合string，check每个有没有，有就加进去
    movieName = data["movieName"]
    startYear = data["movieYear"]
    director = data["director"]
    writer = data["writer"]
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
    if director is not None:  # need select from Faculty
        where += "directors = %s and "
        val += (director,)
    if writer is not None:  # need select from Faculty
        where += "writers = %s and "
        val += (writer,)
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
        a = list(i)
        return_list.append(a)
    # --------------- retrieve primaryName from Faculty --------------
    faculty_sql = ""
    if director is not None:
        faculty_sql = "select primaryname from faculty where nconst= %s"
        val = (director,)
        print(val)
        cursor.execute(faculty_sql, val)
        result2 = cursor.fetchall()
        print(result2)
        director_name = result2[0][0]
    if writer is not None:
        faculty_sql = "select primaryname from faculty where nconst= %s"
        val = (writer,)
        cursor.execute(faculty_sql, val)
        result3 = cursor.fetchall()
        writer_name = result3[0][0]

    return json.dumps(return_list)
    pass
