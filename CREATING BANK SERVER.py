import mysql.connector as conn
connecting_with_mysql = conn.connect(host='localhost', user='root', password='ketan45@')
cursor = connecting_with_mysql.cursor()
query = 'create database bank_customer'
query1 = 'use bank_customer'
cursor.execute(query)
cursor.execute(query1)

query2 = 'create table customer_info(' \
        'id INT AUTO_INCREMENT,' \
        'name VARCHAR(50) NOT NULL,' \
        'email VARCHAR(50) NOT NULL,' \
        'phone VARCHAR(50),' \
        'gender VARCHAR(10),' \
        'account_type VARCHAR(10),' \
        'account_balance INT,' \
        'account_number INT,' \
        'account_pin INT,' \
        'account_date DATE,' \
        'PRIMARY KEY(id))'

cursor.execute(query2)
connecting_with_mysql.close()
