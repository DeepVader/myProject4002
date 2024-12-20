import matplotlib.pyplot as plt
from prettytable import PrettyTable


def Customer_Segment():
    from db.conn import create_connection, close_connection

    conn = create_connection()
    mycursor = conn.cursor()
    mycursor.execute("SELECT COUNT(customer_id) FROM customers ")
    myresult = mycursor.fetchone()

    print("=" * 70)
    print("Customer Segmentation".center(70, " "))
    print(f"Total customer = {myresult[0]} persons".center(70, " "))
    print("=" * 70)

    mycursor.execute(
        """SELECT customer_id, customer_name, state, city
                    FROM customers;
                    """
    )
    myresult = mycursor.fetchall()

    table = PrettyTable()
    table.field_names = ["Customer ID", "Name", "State", "City"]

    for i, row in enumerate(myresult, start=1):
        table.add_row([row[0], row[1], row[2], row[3]])
    print(table)

    mycursor.execute(
        """SELECT state, COUNT(*) AS state_count
                    FROM customers
                    GROUP BY state
                    ORDER BY state_count DESC;
                    """
    )
    myresult = mycursor.fetchall()

    close_connection(conn)

    states = [row[0] for row in myresult]
    persons = [row[1] for row in myresult]

    plt.figure(figsize=(10, 6))
    plt.bar(states, persons, color="skyblue")
    bars = plt.bar(states, persons, color="skyblue")
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            f"{yval:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("State")
    plt.ylabel("Number of Customer")
    plt.title("Customer Data by State")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()

    print("=" * 70)
