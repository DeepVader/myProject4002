import mysql.connector
from datetime import date
from conn import close_connection, create_connection


def create_member(
    conn,
    first_name,
    last_name,
    phone,
    membership_date=None,
    membership_status_id=1,
):
    if membership_date is None:
        membership_date = date.today()

    try:
        with conn.cursor() as cursor:
            # 2. เพิ่มข้อมูลสมาชิกในตาราง members
            insert_member_query = """
            INSERT INTO members (first_name, last_name, phone, membership_date, membership_status_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(
                insert_member_query,
                (first_name, last_name, phone, membership_date, membership_status_id),
            )
            conn.commit()

            # 3. หาค่า member_id ของสมาชิกที่เพิ่ม
            member_id = cursor.lastrowid

            # 4. เพิ่มข้อมูลในตาราง membership_history
            insert_history_query = """
            INSERT INTO membership_history (member_id, status_id, start_date, end_date)
            VALUES (%s, %s, %s, %s)
            """
            # เนื่องจากเป็นการเริ่มต้นสมาชิกใหม่, end_date จะเป็น NULL
            cursor.execute(
                insert_history_query,
                (member_id, membership_status_id, membership_date, None),
            )
            conn.commit()

            print(f"เพิ่มสมาชิก {first_name} {last_name} สำเร็จ!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_member(conn, "John", "Doe", "1234567890", date(2024, 11, 5), 1)

        close_connection(conn)
