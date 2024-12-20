import mysql.connector


def create_connection(*, use_database=True):
    from db.config import DB_CONFIG

    try:
        if use_database:
            conn = mysql.connector.connect(
                host=DB_CONFIG["host"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
                database=DB_CONFIG["database"],
            )
        else:
            conn = mysql.connector.connect(
                host=DB_CONFIG["host"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
            )
        # print("---" * 7)
        # print("Connection successful")
        # print("---" * 7)
        return conn
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        return None


def close_connection(conn):
    if conn.is_connected():
        conn.close()
        # print("---" * 7)
        # print("Connection closed")
        # print("---" * 7)
