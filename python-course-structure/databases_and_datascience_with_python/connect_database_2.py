import psycopg2


def connect_to_db():
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'sample_database'
    db_user = 'postgres'
    db_password = 'Sanjana.25'

    return psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
    print("Successfully connected to the database")


if __name__ == '__main__':
    connect_to_db()
