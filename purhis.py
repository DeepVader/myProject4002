from conn import create_connection, close_connection


def purHis(data):
    c_data = data
    print(c_data)
    hist = getOneCHis(data)

    print("purchase history")
    print(hist)


def getOneCHis(data):
    c_data = data[0]
    conn = create_connection()

    if conn:
        mycursor = conn.cursor()

        val = c_data
        sql = f"""select od.order_id, o.order_date, od.amount, od.quantity, cat.category_name, sub.subcategory_name
from orderdetails as od
	JOIN orders as o
    ON od.order_id = o.order_id
	JOIN subcategories as sub
    ON  od.subcategory_id = sub.subcategory_id
	JOIN categories as cat
    ON sub.category_id = cat.category_id
WHERE o.customer_id = {val};
"""
        # val = c_data

        mycursor.execute(sql)
        result = mycursor.fetchall()

        close_connection(conn)

        if result:
            return result
        else:
            result = (0, 0, 0, 0)
            return result
    else:
        print("Connection is not open.")


if __name__ == "__main__":
    val = 2
    purHis(val)
