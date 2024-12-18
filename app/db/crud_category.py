import mysql.connector


def read_all_cat_from_db():
    from db.conn import create_connection

    query = "SELECT * FROM Categories"
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows:
                    columns = [column[0] for column in cursor.description]
                    return rows, columns
                else:
                    return None, None
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        return None, None


def read_one_cat_from_db(val):
    from db.conn import create_connection

    query = "SELECT * FROM Categories WHERE Category_ID = %s"
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                rows = cursor.fetchall()
                if rows:
                    columns = [column[0] for column in cursor.description]
                    return rows, columns
                else:
                    return None, None
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        return None, None


def create_one_cat_from_db(val):
    from db.conn import create_connection

    query = "INSERT INTO Categories (Category_Name) VALUES (%s)"
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                conn.commit()
                last_inserted_id = cursor.lastrowid
                if last_inserted_id is not None:
                    from db.crud_category import read_one_cat_from_db

                    return read_one_cat_from_db((str(last_inserted_id),))
                return None, None
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        return None, None


def edit_one_cat_from_db(val):
    from db.conn import create_connection

    query = "UPDATE Categories SET Category_Name = %s WHERE Category_ID = %s"
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                conn.commit()
                if cursor.rowcount > 0:  # Check if any rows were affected
                    from db.crud_category import read_one_cat_from_db

                    return read_one_cat_from_db((val[1],))
                return None, None
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        return None, None


def delete_one_cat_from_db(val):
    from db.conn import create_connection

    query = "DELETE FROM Categories WHERE Category_ID = %s"
    try:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, val)
                conn.commit()
                if cursor.rowcount > 0:
                    from db.crud_category import read_all_cat_from_db

                    return read_all_cat_from_db()
                return None, None
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        return None, None
