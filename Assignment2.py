from tkinter import *
import random
import sqlite3
from PUT import CREATETABLE

conn=sqlite3.connect('showdata.sqlite')
cur=conn.cursor()

try:
    cur.execute('SELECT name FROM Shows')
except:
    CREATETABLE()


cur.execute('SELECT name FROM Shows ORDER BY RANDOM() LIMIT 10')
listofshows=list()
listofshowsmixed=list()
score=0

for i in range(0,10):
    scrambled=''
    name=cur.fetchone()[0]
    listofshows.append(name)
    if ' ' not in name:
        scrambled=''.join(random.sample(name,len(name)))
    if ' ' in name:
        temp=name.split()
        for i in temp:
            scrambled=scrambled+''.join(random.sample(i,len(i)))+' '
        scrambled.strip()
    scrambled=scrambled.lower()
    listofshowsmixed.append(scrambled)


for i in range(0,10):
    print('Name number ',i+1,':')
    print(listofshowsmixed[i])
    print('Enter your guess: ')
    guess=input()
    if(guess.lower()==listofshows[i].lower()):
        score+=1
        print('Correct!')
    else:
        print('Wrong!')

print('You scored ',score,'.')
