import pymysql

class Database:
    def __init__(self):
        # MySQL Connection 연결
        self.connect = pymysql.connect(host='127.0.0.1',
                                       port=3306,
                                      user='root',
                                      password='!jukitty950918',
                                      db='cat', charset='utf8')  # 한글처리 (charset = 'utf8')

        # Connection 으로부터 Cursor 생성
        self.cursor = self.connect.cursor()

    def getData(self, table_name, option=None):
        ret = []
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

        #### only one Table ###
        # for e in rows:
        #     temp = {'data_id': e[0], 'animal_type': e[1],
        #             'animal_act': e[2], 'data_address': e[3],
        #             'animal_timestamp': e[4]}
        #     print(e)
        #     ret.append(temp)
        # return ret

    def insData(self, table_name, values):
        curs = self.cursor
        option = ''
        for o in values:
            option += '%s,'
        option = option[:-1]

        sql = f"INSERT INTO {table_name}   " \
               f"VALUES ({option});"

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

    def delData(self, table_name, data_id):
        curs = self.cursor
        sql = f'delete from {table_name} where data_id=%s'
        curs.execute(sql, data_id)
        self.connect.commit()
        self.connect.close()

if __name__ == '__main__':
    # datalist = Database()
    # datalist = Database().insDate('aaa', 'bb', 'cc', 'dd')
    # datalist = Database().updDate('aa', 'dd', 'dd', 'aa')
    datalist = Database().delData(table_name='webcam_data', data_id=4)
    # datalist = Database().insData(table_name='webcam_data',values=[44, 'cat', 'sit', './temp\\frame_20230315_162017.jpg', '2023-03-15 16:20:17'])
    print(datalist)
    '''
(0, 'cat', 'sit', './temp\\frame_20230315_162017.jpg', '2023-03-15 16:20:17')
(1, 'dog', 'sit', './frame_image\\frame_20230315_171506.jpg', '2023-03-15 17:15:06')
[{'data_id': 0, 'animal_type': 'cat', 'animal_act': 'sit', 'data_address': './temp\\frame_20230315_162017.jpg', 'animal_timestamp': '2023-03-15 16:20:17'}, {'data_id': 1, 'animal_type': 'dog', 'animal_act': 'sit', 'data_address': './frame_image\\frame_20230315_171506.jpg', 'animal_timestamp': '2023-03-15 17:15:06'}]
    '''
