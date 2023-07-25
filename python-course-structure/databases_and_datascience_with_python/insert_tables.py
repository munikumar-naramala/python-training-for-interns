from connect_sql import cursor, cnx
import mysql.connector


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format('my_test_db'))
    except mysql.connector.Error as error:
        print("Failed creating database: {}".format(error))
        exit(1)


try:
    cursor.execute("USE {}".format('my_test_db'))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format('my_test_db'))

    create_database(cursor)
    print("Database {} created successfully.".format('my_test_db'))
    cnx.database = 'my_test_db'
