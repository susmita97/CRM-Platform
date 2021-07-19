import pymysql

conn = pymysql.connect(database = 'employees', host='localhost', user = 'susmita', password = 'susmita12')
cursor = conn.cursor()
cursor.execute('select *from employees;')
