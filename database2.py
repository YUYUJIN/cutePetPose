import pymysql
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Database:
    def __init__(self):
        # MySQL Connection 연결
        self.connect = pymysql.connect(host='',
                                       port=,
                                      user='',
                                      password='',
                                      db='', charset='utf8')  # 한글처리 (charset = 'utf8')

        # Connection 으로부터 Cursor 생성
        self.cursor = self.connect.cursor()

    def getData(self, table_name, option=None):
        curs = self.cursor

        if option == None:
            sql = f"select * from {table_name};"
        else:
            sql = f"select * from {table_name} where {option};"

        curs.execute(sql)
        rows = curs.fetchall()
        self.connect.commit()
        self.connect.close()
        return rows

    def insData(self, values):
        curs = self.cursor

        sql = "INSERT INTO animal_data (animal_type, animal_act, animal_address, animal_timestamp) " \
              "VALUES (%s, %s, %s, default)"

        # print(sql)
        curs.execute(sql, values)
        self.connect.commit()
        self.connect.close()

    def updData(self, table_name, values):
        curs = self.cursor
        option = ''
        for o in values:
            option += '%s,'
        option = option[:-1]

        sql = f"update INTO {table_name}   " \
              f"VALUES ({option});"
        curs.execute(sql, values)
        self.connect.commit()
        self.connect.close()

    def delData(self, table_name, animal_id):
        curs = self.cursor
        sql = f'delete from {table_name} where animal_id=%s'
        curs.execute(sql, animal_id)
        self.connect.commit()
        self.connect.close()


    def getCountByTimeRange(self, table_name):
        curs = self.connect.cursor()

        try:
            # animal_id의 최소값과 최대값에 해당하는 데이터의 animal_timestamp 값을 가져옴
            sql = f"SELECT MIN(animal_timestamp), MAX(animal_timestamp) FROM {table_name} " \
                  f"WHERE animal_id = (SELECT MIN(animal_id) FROM {table_name}) " \
                  f"OR animal_id = (SELECT MAX(animal_id) FROM {table_name})"
            curs.execute(sql)
            animal_timestamps = curs.fetchone()
            start_timestamp = animal_timestamps[0]
            end_timestamp = animal_timestamps[1]

            # time range 내 animal_act별 count 계산
            sql = f"SELECT animal_act, COUNT(*) FROM {table_name} " \
                  f"WHERE animal_timestamp >= %s AND animal_timestamp < %s GROUP BY animal_act"
            curs.execute(sql, (start_timestamp, end_timestamp))
            data = curs.fetchall()

            # act_count 테이블에 insert 또는 update
            for row in data:
                # 중복된 값 체크
                sql = "SELECT animal_count FROM act_count WHERE animal_act=%s"
                val = (row[0],)
                curs.execute(sql, val)
                result = curs.fetchone()
                if result:
                    # 이미 존재하는 row의 count 값을 업데이트
                    sql = "UPDATE act_count SET animal_count=animal_count+%s WHERE animal_act=%s"
                    val = (row[1], row[0])
                    curs.execute(sql, val)
                else:
                    # 새로운 row를 추가함
                    sql = "INSERT INTO act_count (animal_act, animal_count) VALUES (%s, %s)"
                    val = (row[0], row[1])
                    curs.execute(sql, val)

            # 데이터베이스에 변경사항 저장
            self.connect.commit()

        finally:
            # 데이터베이스 연결 종료
            curs.close()
            self.connect.close()
