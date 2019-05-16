import sqlite3

def CREATETABLE():
    conn=sqlite3.connect("showdata.sqlite")
    cur=conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS Shows;

    CREATE TABLE Shows(
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    )
    ''')

    i=''
    n=1
    for n in range(0,30):
        print('INPUT ',n+1,' :',end='')
        i=input()
        cur.execute('INSERT INTO Shows (name) VALUES (?)',(i,))
        n+=1
        conn.commit()
    conn.close()

