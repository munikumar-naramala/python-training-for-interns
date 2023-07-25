import sqlite3


def connect_to_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def insert_data(conn, table_name, data):
    cursor = conn.cursor()
    query = f"INSERT INTO {table_name} (column1, column2, ...) VALUES (?, ?, ...)"
    cursor.execute(query, data)
    conn.commit()


def update_data(conn, table_name, data, condition):
    cursor = conn.cursor()
    query = f"UPDATE {table_name} SET column1 = ?, column2 = ... WHERE {condition}"
    cursor.execute(query, data)
    conn.commit()


def delete_data(conn, table_name, condition):
    cursor = conn.cursor()
    query = f"DELETE FROM {table_name} WHERE {condition}"
    cursor.execute(query)
    conn.commit()


if __name__ == '__main__':
    connect_to_database('my_test_db')
