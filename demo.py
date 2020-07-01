import pandas as pd
import csv
import json

path = 'files\\'
file_name = 'teachers.parquet'
file_name1 = 'teachers.csv'
file_name2 = 'students.csv'

csv_file_name = file_name.split('.')[0]+'.csv'
df = pd.read_parquet(path+file_name)
df.to_csv(path+csv_file_name, index=False)

with open(path+file_name2, "r") as student_file, open(path+file_name1, 'r') as teacher_file:
    student_reader = csv.DictReader(student_file, delimiter='_')
    teacher_reader = csv.reader(teacher_file, delimiter=',')

    data = []
    student_list = []

    for line in teacher_reader:
        if line[0] != 'id':
            data.append(line)

    for j, row in enumerate(student_reader):
        for dat in data:
            if dat[-1] == row.get('cid'):
                row['teacher']=dat[1]+' '+dat[2]
                student_list.append(dict(row))

with open(path+'output.json', 'w') as json_file:
    json.dump(student_list, json_file)
