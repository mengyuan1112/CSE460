from asyncore import read
from click import command
import psycopg2
import csv
import sys
import flask

'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
'''
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cursor = conn.cursor()
commands = [
    """
    CREATE TABLE IF NOT EXISTS Faculty(
        nconst VARCHAR(255) UNIQUE,
        primaryName VARCHAR(255),
        PRIMARY KEY (nconst)
    )
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS Movie(
        tconst VARCHAR(255) UNIQUE,
        startYear INTEGER,
        primaryTitle VARCHAR(255),
        runtimeMinutes Integer,
        averageRating FLOAT,
        numVotes Integer,
        isAdult INTEGER,
        genres VARCHAR(255),
        directors VARCHAR(255),
        writers VARCHAR(255),
        PRIMARY KEY (tconst)
    )
    """
]


def create_table():
    for command in commands:
        cursor.execute(command)
    conn.commit()
    return


def insert_data():
    cursor = conn.cursor()
    with open("file/title.basics.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        next(tsv_file)
        count = 0
        for i in tsv_file:
            try:
                runtime = int(i[7])
            except:
                runtime = None
            count += 1
            sql = 'insert into Movie (tconst, primaryTitle, isAdult, startYear, runtimeMinutes, genres) values (%s,%s,%s,%s,%s,%s)'
            val = (i[0], i[2], int(i[4]), int(i[5]), runtime, i[8])
            cursor.execute(sql, val)
            conn.commit()
            if count == 300:
                break
    with open("file/name.basics.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        next(tsv_file)
        count = 0
        for i in tsv_file:
            count += 1
            sql = 'insert into Faculty (nconst, primaryName) values (%s,%s)'
            val = (i[0], i[1])
            cursor.execute(sql, val)
            conn.commit()
            if count == 300:
                break
    with open("file/title.crew.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        next(tsv_file)
        count = 0
        for i in tsv_file:
            count += 1
            if(i[1]=="\\N"):
                i[1]=None
            if (i[2] == "\\N"):
                i[2] = None
            sql = 'Update Movie set directors=%s, writers=%s where tconst=%s'
            val = (i[1], i[2], i[0])
            cursor.execute(sql, val)
            conn.commit()
            if count == 300:
                break
    with open("file/title.ratings.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        next(tsv_file)
        count = 0
        for i in tsv_file:
            count += 1
            try:
                averageRating=float(i[1])
            except:
                averageRating=None
            try:
                numVotes=int(i[2])
            except:
                numVotes=None
            sql = 'Update Movie set averageRating=%s, numVotes=%s where tconst=%s'
            val = (averageRating, numVotes, i[0])
            cursor.execute(sql, val)
            conn.commit()
            if count == 300:
                break
    conn.close()

def drop():
    cursor = conn.cursor()
    sql = "drop TABLE IF EXISTS Movie"
    cursor.execute(sql)
    conn.commit()
    sql = "drop TABLE IF EXISTS Faculty"
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    # python3 app.py <type> <file_path>

    # rating - python3 app.py ratings /Users/mengyuan/Downloads/MovieData/title.ratings.tsv
    # wirter and director - python3 app.py people /Users/mengyuan/Downloads/MovieData/title.crew.tsv
    # people info - python3 app.py info /Users/mengyuan/Downloads/MovieData/name.basics.tsv
    # movie - python3 app.py movie /Users/mengyuan/Downloads/MovieData/title.basics.tsv

    #print(sys.argv)
    #table = sys.argv[1]
    #path = sys.argv[2]
    drop()
    create_table()
    insert_data()
