import mysql.connector
import os
import pandas as pd
from db.config import DB_NAME, TABLES
from db.conn import create_connection, close_connection


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


def import_csv_to_db(conn, table_name, csv_file):
    df = pd.read_csv(csv_file)
    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    insert_query = f"""
        INSERT INTO {table_name} ({columns})
        VALUES ({placeholders})
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"USE {DB_NAME}")
            for row in df.itertuples(index=False, name=None):
                cursor.execute(insert_query, row)
            conn.commit()
            print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    data = [
        ("Customers", "customers_df.csv"),
        ("Categories", "categories_df.csv"),
        ("SubCategories", "subcategories_df.csv"),
        ("Orders", "orders_table.csv"),
        ("OrderDetails", "order_details_table.csv"),
        # ("SalesTargets", "sales_targets_table.csv"),
    ]
    folder_path = "./datatrans/"

    conn = create_connection(use_database=False)
    if conn:
        create_database(conn)
        create_tables(conn)

        for table_name, csv_file in data:
            csv_file_path = os.path.join(folder_path, csv_file)
            import_csv_to_db(conn, table_name, csv_file_path)

        close_connection(conn)
    else:
        print("Connection is not open.")
