from getpass import getpass
from conn import create_connection, close_connection


def signup():
    print("=" * 50)
    print("Sign up:")

    # input
    user = input("_Name: ")
    password = getpass("_password: ")
    state = input("_State: ")
    city = input("_City: ")

    c_dict = {
        "Customer_Name": user,
        "Customer_Password": password,
        "State": state,
        "City": city,
    }

    id_c = create_customer(c_dict)

    print("new c: ", id_c)


def create_customer(data):
    conn = create_connection()
    tuple_rep = tuple(data.values())

    if conn:
        mycursor = conn.cursor()

        sql = "INSERT INTO customers (Customer_Name, Customer_Password, State, City) VALUES (%s, %s, %s, %s)"
        val = tuple_rep

        mycursor.execute(sql, val)
        conn.commit()

        close_connection(conn)

        return mycursor.lastrowid
    else:
        print("Connection is not open.")


if __name__ == "__main__":
    signup()
