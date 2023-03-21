import json
from datetime import datetime, timedelta

def today(self, table_name, animal_type, output_file):
    curs = self.connect.cursor()

    # animal_id의 최대값에 해당하는 데이터의 animal_timestamp 값을 가져옴
    sql = f"SELECT MAX(animal_timestamp) FROM {table_name}"
    curs.execute(sql)
    max_animal_timestamp = curs.fetchone()[0]

    # 최대 animal_timestamp 기준으로 24시간 이전 시간대 구하기
    start_time = max_animal_timestamp - timedelta(days=1)
    end_time = max_animal_timestamp

    # time range 내 animal_act별 count 계산
    sql = f"SELECT animal_type, animal_act, HOUR(animal_timestamp), COUNT(*) FROM {table_name} " \
          f"WHERE animal_type = {animal_type} AND animal_timestamp >= %s AND animal_timestamp <= %s GROUP BY animal_act, HOUR(animal_timestamp)"
    curs.execute(sql, (start_time, end_time))
    data = curs.fetchall()

    result = []
    for row in data:
        animal_act = row[1]
        hour = row[2]
        count = row[3]
        found = False
        for item in result:
            if item['id'] == animal_act:
                found = True
                item['data'].append({'x': str(hour), 'y': count})
                break
        if not found:
            result.append({'id': animal_act, 'data': [{'x': str(hour), 'y': count}]})

    output = {
        'keys': 'day',
        'label': '하루',
        'data': result
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)



def dailyPi(self, table_name, animal_type, output_file):
    curs = self.connect.cursor()

    # animal_id의 최소값과 최대값에 해당하는 데이터의 animal_timestamp 값을 가져옴
    sql = f"SELECT MIN(animal_timestamp), MAX(animal_timestamp) FROM {table_name}"
    curs.execute(sql)
    animal_timestamps = curs.fetchone()
    start_timestamp = animal_timestamps[0]
    end_timestamp = animal_timestamps[1]

    # time range 내 animal_act별 count 계산
    sql = f"SELECT animal_type, animal_act, DATE(animal_timestamp), COUNT(*) FROM {table_name} " \
          f"WHERE animal_type = {animal_type} AND animal_timestamp >= %s AND animal_timestamp <= %s GROUP BY animal_type, animal_act, DATE(animal_timestamp)"
    curs.execute(sql, (start_timestamp, end_timestamp))
    data = curs.fetchall()

    result = []
    for row in data:
        animal_act = row[1]
        count = row[3]
        result.append({'id': animal_act, 'value': count})

    output = {
        'keys': 'day',
        'data': result
    }
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

def weeklyPi(self, table_name, animal_type, output_file):
    curs = self.connect.cursor()

    # animal_id의 최소값과 최대값에 해당하는 데이터의 animal_timestamp 값을 가져옴
    sql = f"SELECT MIN(animal_timestamp), MAX(animal_timestamp) FROM {table_name}"
    curs.execute(sql)
    animal_timestamps = curs.fetchone()
    start_timestamp = animal_timestamps[0]
    end_timestamp = animal_timestamps[1]

    # time range 내 animal_act별 count 계산
    sql = f"SELECT animal_type, animal_act, DATE(animal_timestamp), HOUR(animal_timestamp), COUNT(*) " \
          f"FROM {table_name} " \
          f"WHERE animal_type = {animal_type} AND animal_timestamp >= %s AND animal_timestamp <= %s " \
          f"GROUP BY animal_type, animal_act, DATE(animal_timestamp), HOUR(animal_timestamp)"
    curs.execute(sql, (start_timestamp, end_timestamp))
    data = curs.fetchall()

    # 주 단위 데이터 생성
    result = {}
    for row in data:
        animal_type = row[0]
        animal_act = row[1]
        date = datetime.strptime(str(row[2]), '%Y-%m-%d')
        hour = str(row[3])
        count = row[4]

        # 주 단위 데이터 생성
        week_start = (date - timedelta(days=date.weekday())).strftime('%Y-%m-%d')
        if week_start in result:
            if animal_act in result[week_start]:
                result[week_start][animal_act] += count
            else:
                result[week_start][animal_act] = count
        else:
            result[week_start] = {animal_act: count}

    data = [{'id': animal_act,
                    'value': sum(result[week_start].get(animal_act, 0) for week_start in result)} for
                   animal_act in
                   set(animal_act for week_start in result for animal_act in result[week_start])]

    output = {
        'keys': 'week',
        'data': data
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

def monthlyPi(self, table_name, animal_type, output_file):
    curs = self.connect.cursor()

    # animal_id의 최소값과 최대값에 해당하는 데이터의 animal_timestamp 값을 가져옴
    sql = f"SELECT MIN(animal_timestamp), MAX(animal_timestamp) FROM {table_name}"
    curs.execute(sql)
    animal_timestamps = curs.fetchone()
    start_timestamp = animal_timestamps[0]
    end_timestamp = animal_timestamps[1]

    # time range 내 animal_act별 count 계산
    sql = f"SELECT animal_type, animal_act, YEAR(animal_timestamp), MONTH(animal_timestamp), HOUR(animal_timestamp), COUNT(*) " \
          f"FROM {table_name} " \
          f"WHERE animal_type = {animal_type} AND animal_timestamp >= %s AND animal_timestamp <= %s " \
          f"GROUP BY animal_type, animal_act, YEAR(animal_timestamp), MONTH(animal_timestamp), HOUR(animal_timestamp)"
    curs.execute(sql, (start_timestamp, end_timestamp))
    data = curs.fetchall()

    # 월 단위 데이터 생성
    result = {}
    for row in data:
        animal_type = row[0]
        animal_act = row[1]
        year = str(row[2])
        month = str(row[3])
        hour = str(row[4])
        count = row[5]

        # 월 단위 데이터 생성
        month_start = f"{year}-{month}-01"
        if month_start in result:
            if animal_act in result[month_start]:
                result[month_start][animal_act] += count
            else:
                result[month_start][animal_act] = count
        else:
            result[month_start] = {animal_act: count}

    data = [{'id': animal_act, 'value': sum(result[month_start].get(animal_act, 0) for month_start in result)} for
            animal_act in set(animal_act for month_start in result for animal_act in result[month_start])]

    output = {
        'keys': 'month',
            'data': data
        }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
