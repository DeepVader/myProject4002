import mysql.connector
from config import DB_NAME, TABLES, myMembershipStatus
from conn import create_connection, close_connection


def create_database(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database {DB_NAME} created or already exists")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def create_tables(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"USE {DB_NAME}")
            for table_name, create_table_sql in TABLES.items():
                cursor.execute(create_table_sql)
                print(f"Table {table_name} created successfully")
            conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def create_status(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"USE {DB_NAME}")
            cursor.execute(myMembershipStatus)
            print("Data inserted successfully!")
            conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    conn = create_connection(use_database=False)
    if conn:
        create_database(conn)
        create_tables(conn)

        create_status(conn)

        close_connection(conn)
