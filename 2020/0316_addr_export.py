import sqlite3

con = sqlite3.connect('C:/Users/PARK/Downloads/보건복지부.db')
cur = con.cursor()

body = ''

for i in cur.execute('SELECT * FROM addr'):
    line = ''
    for j in i:
        line = line + str(j) + ', '
    body = body + line[:-2] + "\n"

f=open('addr_nan308.csv','w')
f.write(body)
f.close
cur.close()
print('csv file export done')