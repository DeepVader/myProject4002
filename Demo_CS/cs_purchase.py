import matplotlib.pyplot as plt
from prettytable import PrettyTable


def Customer_Purchase():
    from db.conn import create_connection, close_connection

    conn = create_connection()
    mycursor = conn.cursor()
    mycursor.execute("SELECT COUNT(customer_id) FROM customers ")
    myresult = mycursor.fetchone()

    print("=" * 63)
    print("Customer Purchase".center(63, " "))
    print(f"Total customer = {myresult[0]} persons".center(63, " "))
    print("=" * 63)

    mycursor.execute(
        """SELECT 
                    c.Customer_ID, 
                    c.Customer_Name, 
                    SUM(od.Quantity) AS Total_Quantity,
                    SUM(od.Amount) AS Total_Amount
                    FROM customers AS c
                    JOIN orders AS o 
                    ON c.Customer_ID = o.Customer_ID
                    JOIN orderdetails AS od 
                    ON o.Order_ID = od.Order_ID
                    GROUP BY 
                    c.Customer_ID, 
                    c.Customer_Name;
                    """
    )
    myresult = mycursor.fetchall()

    table = PrettyTable()
    table.field_names = ["Customer ID.", "Name", "Total Quantity", "Total Amount"]

    for i, row in enumerate(myresult, start=1):
        table.add_row([row[0], row[1], row[2], row[3]])

    print(table)

    mycursor.execute(
        """SELECT 
                    c.Customer_Name, 
                    SUM(od.Amount) AS Total_Amount
                    FROM customers AS c
                    JOIN orders AS o 
                    ON c.Customer_ID = o.Customer_ID
                    JOIN orderdetails AS od 
                    ON o.Order_ID = od.Order_ID
                    GROUP BY c.Customer_Name
                    ORDER BY Total_Amount DESC
                    LIMIT 10;
                    """
    )
    results = mycursor.fetchall()

    close_connection(conn)

    customer_names = [row[0] for row in results]
    total_amounts = [row[1] for row in results]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(customer_names, total_amounts, color="skyblue")
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 10,
            f"{yval:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.bar(customer_names, total_amounts, color="skyblue")
    plt.xlabel("Customer Name")
    plt.ylabel("Total Amount")
    plt.title("Top 10 Customers by Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print("=" * 50)
