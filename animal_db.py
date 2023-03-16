import pymysql
import os
from datetime import datetime
from flask import request

# MySQL Connection 연결
connect = pymysql.connect(host='',
                      user='',
                      password='',
                      db='', charset='utf8')  # 한글처리 (charset = 'utf8')

# Connection 으로부터 Cursor 생성
cursor = connect.cursor()

# 이미지 저장 경로
os.makedirs('./frame_image', exist_ok=True)

image_path = './frame_image'

# 데이터 삽입 SQL 쿼리
sql = "INSERT INTO webcam_data (data_id, animal_type, animal_action, data_address, animal_timestamp) " \
      "VALUES (%s, %s, %s, %s, %s, %s)"


# 삽입할 데이터
data_id = 3
animal_type = 'dog'
animal_action = 'sit'

current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
image_file = f'frame_{current_time}.jpg'
data_address = os.path.join(image_path, image_file)

animal_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = (data_id, animal_type, animal_action, data_address, animal_timestamp)

try:
    # 이미지 데이터 저장
    # image = request.files.get('image')
    # image.save(data_address)

    # 쿼리 실행
    cursor.execute(sql, data)

    # 변경 내용을 DB에 반영
    connect.commit()

except Exception as e:
    # 에러 발생 시 변경 내용을 되돌리고 예외 처리
    connect.rollback()
    print('Error:', e)

finally:
    # DB 연결 종료
    connect.close()