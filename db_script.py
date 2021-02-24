import csv
import sqlite3

con = sqlite3.connect("db.sqlite3")
curs = con.cursor()
# curs.execute("drop table api_yamdb_genres;")
curs.execute(
    "create table api_yamdb_genres("
    "id integer "
    "primary key autoincrement, "
    "name varchar(50) not null "
    "unique, "
    "slug varchar(50) not null "
    "unique "
    ");"
)
with open('data/genre.csv', 'r') as file:
    dr = csv.DictReader(file,)
    to_db = [(i['id'], i['name'], i['slug']) for i in dr]

curs.executemany(
    "INSERT INTO api_yamdb_genres ('id', 'name', 'slug') VALUES (?, ?, ?);",
    to_db
)
con.commit()
con.close()
