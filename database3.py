import pymysql
import json

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
        # self.connect.close()
        return rows

    def insData(self, values):
        curs = self.cursor

        sql = "INSERT INTO animal_data (animal_type, animal_act, animal_address, animal_timestamp) " \
              "VALUES (%s, %s, %s, default)"

        # print(sql)
        curs.execute(sql, values)
        self.connect.commit()
        # self.connect.close()

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
        # self.connect.close()

    def delData(self, table_name, animal_id):
        curs = self.cursor
        sql = f'delete from {table_name} where animal_id=%s'
        curs.execute(sql, animal_id)
        self.connect.commit()
        # self.connect.close()

    def getCountByTimeRange(self, table_name, output_file):
        curs = self.connect.cursor()

        # animal_id의 최소값과 최대값에 해당하는 데이터의 animal_timestamp 값을 가져옴
        sql = f"SELECT MIN(animal_timestamp), MAX(animal_timestamp) FROM {table_name}"
        curs.execute(sql)
        animal_timestamps = curs.fetchone()
        start_timestamp = animal_timestamps[0]
        end_timestamp = animal_timestamps[1]

        # time range 내 animal_act별 count 계산
        sql = f"SELECT animal_type, animal_act, HOUR(animal_timestamp), COUNT(*) FROM {table_name} " \
              f"WHERE animal_timestamp >= %s AND animal_timestamp < %s GROUP BY animal_type, animal_act, HOUR(animal_timestamp)"
        curs.execute(sql, (start_timestamp, end_timestamp))
        data = curs.fetchall()

        # 결과를 json 파일로 저장
        result = {}
        for row in data:
            animal_type = row[0]
            animal_act = row[1]
            hour = str(row[2])
            count = row[3]
            if animal_type not in result:
                result[animal_type] = {}
            if animal_act not in result[animal_type]:
                result[animal_type][animal_act] = {}
            result[animal_type][animal_act][hour] = count
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=4)

        # 데이터베이스에 변경사항 저장
        self.connect.commit()

    def db_disconnect(self):
        self.connect.close()
