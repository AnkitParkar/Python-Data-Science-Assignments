import json
import sqlite3

conn=sqlite3.connect('patientdata.sqlite')
cur=conn.cursor()

fname='asdf.txt'
strdata = open(fname).read()
data = json.loads(strdata)

cur.executescript('''
DROP TABLE IF EXISTS Records;

CREATE TABLE Records(
    age INTEGER,
    sex INTEGER,
    cp INTEGER,
    trestbps INTEGER,
    chol INTEGER,
    fbs INTEGER,
    restecg INTEGER,
    thalach INTEGER,
    exang INTEGER,
    oldpeak INTEGER,
    slope INTEGER,
    ca INTEGER,
    thal INTEGER
)
''')

for i in data['records']:
    cur.execute('INSERT INTO Records (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',(i['age'],i['sex'],i['cp'],i['trestbps'],i['chol'],i['fbs'],i['restecg'],i['thalach'],i['exang'],i['oldpeak'],i['slope'],i['ca'],i['thal']))
    conn.commit()
conn.close()    
                                                    
