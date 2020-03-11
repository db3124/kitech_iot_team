import pymysql
import pymysql.cursors

mydb = pymysql.connect(
    host='localhost',
    user='kite',
    password='admin',
    db='project',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

with mydb:
    cur = mydb.cursor()
    
    cur.execute("SELECT * FROM guestbook")

    rows = cur.fetchall()

    for row in rows:
        print(row["idx"], row["title"])

print(mydb)