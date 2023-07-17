import pymysql

# Establish a connection
cnx = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Sanjana.25',
    database='my_test_db'
)

if cnx:
    print('connection successful')

cursor = cnx.cursor()