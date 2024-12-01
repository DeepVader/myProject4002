from getpass import getpass
from conn import create_connection, close_connection
from menuShop import menuShop


def login():
    print("=" * 50)
    print("Login:")

    # input
    user = input("_Name: ")
    password = getpass("_password: ")

    c_dict = {
        "Customer_Name": user,
        "Customer_Password": password,
    }
    c_data = login_customer(c_dict)
    print(c_data)

    # conditions
    if user == c_data[1] and password == c_data[2]:
        print("OK")
        menuShop(c_data)
    else:
        print("Noob!")


def login_customer(data):
    conn = create_connection()
    tuple_rep = tuple(data.values())

    if conn:
        mycursor = conn.cursor()

        sql = "SELECT * FROM customers WHERE Customer_Name = %s AND Customer_Password = %s"
        val = tuple_rep

        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        close_connection(conn)

        if result:
            return result
        else:
            result = (0, 0, 0, 0)
            return result
    else:
        print("Connection is not open.")


if __name__ == "__main__":
    login()
