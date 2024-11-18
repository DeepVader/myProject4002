import mysql.connector
from conn import close_connection, create_connection


def read_status(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT status_id, status_name FROM membership_status")
            fetch_data = cursor.fetchall()
            return fetch_data
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        x = read_status(conn)
        myresult = dict(x)
        print(myresult)

        close_connection(conn)
