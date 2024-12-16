import pandas as pd


def pd_readSQL_fromDB(query):
    from db.conn import create_connection, close_connection

    conn = create_connection()
    df = pd.read_sql(query, conn)
    close_connection(conn)
    return df


def get_maxWeek_fromDB():
    from db.conn import create_connection, close_connection

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(WEEK(Order_Date)) FROM Orders;")
    max_weeks = cursor.fetchone()[0]
    close_connection(conn)
    return max_weeks
