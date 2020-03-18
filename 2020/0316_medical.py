import sqlite3, csv, datetime

data = open('C:/Users/PARK/Downloads/보건복지부_선별진료소_현황_주소_20200313.csv','r')
data = data.readlines()
con = sqlite3.connect('C:/Users/PARK/Downloads/보건복지부.db')
sqlite3.Connection
cur = con.cursor()
print(datetime.datetime.now())
cur.execute("create table medical(연번 int, 검체채취_가능여부 text, 시도 text, 시군구 text, 의료기관명 text, 주소 text, 대표_전화번호 text,입력자 text, 입력일자 text)")

for i in data[1:]:
    use_data = list(map(str,i.split('\n')))
    use_data = use_data[0].split(',')
    if use_data[5][0] == "\"":
        while use_data[5][-1] != "\"":
            use_data[5] = use_data[5] + ", " + use_data.pop(6)
    if use_data[6][0] == "\"":
        while use_data[6][-1] != "\"":
            use_data[6] = use_data[6] + ", " + use_data.pop(7)
        
    cur.execute(f"insert into medical values({use_data[0]},'{use_data[1]}','{use_data[2]}','{use_data[3]}','{use_data[4]}','{use_data[5]}','{use_data[6]}','nan308@naver.com','{datetime.datetime.now()}')")
con.commit()
