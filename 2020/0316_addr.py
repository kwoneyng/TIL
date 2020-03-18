import sqlite3, csv, datetime

data = open('C:/Users/PARK/Downloads/202002_주소DB_전체분/개선_도로명코드_전체분.txt','r')
data = data.readlines()
con = sqlite3.connect('C:/Users/PARK/Downloads/보건복지부.db')
sqlite3.Connection
cur = con.cursor()
# print(datetime.datetime.now())
cur.execute("create table addr(도로명_코드 int, 도로명 text, 읍면동일련번호 text, 시도명 text, 입력자 text, 입력일자 text)")
for i in data:
    use_data = list(map(str,i.split('|')))
    if use_data[4] == '서울특별시':
        # print(use_data[0],use_data[1],use_data[3],use_data[4])
        cur.execute(f"insert into addr values({use_data[0]},'{use_data[1]}','{use_data[3]}','{use_data[4]}','nan308@naver.com','{datetime.datetime.now()}')")
con.commit()
