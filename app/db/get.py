import mysql.connector


def fetch_data_from_db(query):
    from db.conn import create_connection

    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows:
                    columns = [column[0] for column in cursor.description]
                    return rows, columns
                else:
                    return [], []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None


def get_max_week():
    from db.conn import create_connection

    query = "SELECT MAX(WEEK(Order_Date)) FROM Orders;"
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            if result is not None:
                return result[0]
            else:
                return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
