import csv
import json

headerlist=list()
data=dict()
data['records']=list()

with open('heart.csv') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    linecount=0
    for row in csvreader:
        if linecount==0:
            linecount=linecount+1
            continue
        linecount=linecount+1
        temp={
            'age':row[0],
            'sex':row[1],
            'cp':row[2],
            'trestbps':row[3],
            'chol':row[4],
            'fbs':row[5],
            'restecg':row[6],
            'thalach':row[7],
            'exang':row[8],
            'oldpeak':row[9],
            'slope':row[10],
            'ca':row[11],
            'thal':row[12]
            }
        print(temp)
        data['records'].append(temp)
        print('Processed ',linecount,' lines')

with open('asdf.txt','w') as asdf:
              json.dump(data,asdf)
