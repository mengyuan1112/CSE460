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
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "123"
    )
cursor = conn.cursor()
commands = [
    """
    CREATE TABLE IF NOT EXISTS Writer(
        nconst VARCHAR(255),
        tconst VARCHAR(255) UNIQUE,
        name VARCHAR(255) UNIQUE,
        knowForTitles text[],
        PRIMARY KEY (nconst)
    )
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS Director(
        nconst VARCHAR(255) UNIQUE,
        tconst VARCHAR(255) UNIQUE,
        name VARCHAR(255) UNIQUE,
        knowForTitles text[],
        PRIMARY KEY (nconst)
    )
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS Ratings(
        tconst VARCHAR(255),
        averageRating FLOAT,
        numVote INTEGER,
        PRIMARY KEY (tconst)
    )
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS Genres(
        primiaryTitle VARCHAR(255),
        isAdult BOOLEAN,
        genres VARCHAR(255),
        PRIMARY KEY (primiaryTitle)
    )
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS Movie(
        primiaryTitle VARCHAR(255),
        tconst VARCHAR(255),
        director VARCHAR(255),
        writer VARCHAR(255),
        startYear INTEGER,
        runtimeMInutes INTEGER,
        language VARCHAR(255),
        genres VARCHAR(255),
        PRIMARY KEY (primiaryTitle),
        FOREIGN KEY (tconst)
            REFERENCES Ratings (tconst)
            ON Delete Set NULL
            ON update CASCADE,
        FOREIGN KEY (primiaryTitle)
            REFERENCES Genres (primiaryTitle)
            ON Delete Set NULL
            ON update CASCADE,
        FOREIGN KEY (writer)
            REFERENCES Writer (nconst)
            ON Delete Set NULL
            ON update CASCADE,
        FOREIGN KEY (director)
            REFERENCES Director (nconst)
            ON Delete Set NULL
            ON update CASCADE
    )
    """
]    
def create_table():    
    for command in commands:
        cursor.execute(command)
    conn.commit()
    return

def insert_data(table, path):
    tsv_file = open(str(path))
    read_file = csv.reader(tsv_file, delimiter="\t")
    count = 0;
    cursor = conn.cursor()
    for row in read_file:
        query = None
        if count == 0: 
            count+=1
            continue
        if(table == 'ratings'): 
            query = "INSERT INTO Ratings (tconst, averageRating, numvote) VALUES (%s, %s, %s);"
            cursor.execute(query, (str(row[0]), float(row[1]), int(row[2])))
            
        if(table == 'people'): 
            director_query = "INSERT INTO director (nconst, tconst) VALUES (%s, %s) ON conflict do nothing;"
            writer_query = "INSERT INTO writer (nconst, tconst) VALUES (%s, %s) ON conflict do nothing;"
            list = row[1].split(",")
            list2 = row[2].split(",")
            for j in list: 
                if(j != "\\N"):cursor.execute(director_query, (j,row[0]))
            for j in list2:
                if(j != "\\N"): cursor.execute(writer_query, (j,row[0]))
        if(table == "info"):
            director_query = "UPDATE director SET name = %s, knowForTitles = %s Where nconst = %s;"
            cursor.execute(director_query, (str(row[1]), [str(row[5])], str(row[0])))
            writer_query = "UPDATE writer SET name = %s, knowForTitles = %s Where nconst = %s;"
            cursor.execute(writer_query, (str(row[1]), [str(row[5])], str(row[0])))
            
        if(table == 'movie'): 
            genre_query = "INSERT INTO Genres (primiaryTitle, isAdult, genres) VALUES (%s, %s, %s) ON conflict do Nothing;"
            cursor.execute(genre_query, (str(row[2]), str(row[4]), str(row[8][0])))
            movie_query = """INSERT INTO Movie (primiarytitle, tconst, startyear, runtimeminutes, genres) VALUES (%s, %s, %s, %s, %s) ON CONFLICT do Nothing;"""
            start, runtime= -1, -1
            if row[5] != "\\N": start = row[5]
            if row[7] != "\\N": start = row[7]
            status = "Select tconst from ratings where %s IN (Select tconst from ratings);"
            s = cursor.execute(status, (row[0],))
            if(s != None): cursor.execute(movie_query, (str(row[2]), str(row[0]), int(start), int(runtime), str(row[8]) ))
            update_director_query = "UPDATE movie Set director = director.nconst From director Where movie.tconst = director.tconst;"
            update_writer_query = "UPDATE movie Set writer = writer.nconst From writer Where movie.tconst = writer.tconst;"
            cursor.execute(update_director_query)
            cursor.execute(update_writer_query)
        
        conn.commit()
        count+=1
        if count == 300: return
    
if __name__ == '__main__':
    # python3 app.py <type> <file_path>

    # rating - python3 app.py ratings /Users/mengyuan/Downloads/MovieData/title.ratings.tsv
    # wirter and director - python3 app.py people /Users/mengyuan/Downloads/MovieData/title.crew.tsv
    # people info - python3 app.py info /Users/mengyuan/Downloads/MovieData/name.basics.tsv
    # movie - python3 app.py movie /Users/mengyuan/Downloads/MovieData/title.basics.tsv

    print(sys.argv)
    table = sys.argv[1]
    path = sys.argv[2]
    
    create_table()
    insert_data(table, path)
    '''
    app.run(host='0.0.0.0', port=8899)
    app.run(debug=True)
    '''



    