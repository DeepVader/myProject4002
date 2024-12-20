import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable


def Demographic_Trends():
    from db.conn import create_connection, close_connection

    conn = create_connection()
    mycursor = conn.cursor()
    mycursor.execute("SELECT COUNT(customer_id) FROM customers ")
    myresult = mycursor.fetchone()

    print("=" * 50)
    print("Demographic Trends".center(50, " "))
    print(f"Total customer = {myresult[0]} persons".center(50, " "))
    print("=" * 50)

    mycursor.execute(
        """
                    SELECT 
                    c.State, 
                    cat.Category_Name, 
                    SUM(od.Quantity) AS Total_Quantity
                    FROM customers c
                    JOIN orders o ON c.Customer_ID = o.Customer_ID
                    JOIN orderdetails od ON o.Order_ID = od.Order_ID
                    JOIN subcategories subcat ON od.SubCategory_ID = subcat.SubCategory_ID
                    JOIN categories cat ON subcat.Category_ID = cat.Category_ID
                    GROUP BY c.State, cat.Category_Name
                    ORDER BY c.State, Total_Quantity DESC;
                    """
    )
    results = mycursor.fetchall()

    close_connection(conn)

    df = pd.DataFrame(results, columns=["State", "Category_Name", "Total_Quantity"])
    df["Total_Quantity"] = pd.to_numeric(df["Total_Quantity"], errors="coerce")
    df["Total_Quantity"] = df["Total_Quantity"].fillna(0)

    df_state_sum = df.groupby("State")["Total_Quantity"].sum().reset_index()
    df_state_sum = df_state_sum.sort_values(by="Total_Quantity", ascending=False)
    df_sorted = df.set_index("State").loc[df_state_sum["State"]].reset_index()

    table = PrettyTable()
    table.field_names = ["State", "Category Name", "Total Quantity"]
    for _, row in df_sorted.iterrows():
        table.add_row([row["State"], row["Category_Name"], row["Total_Quantity"]])
    print(table)

    df_pivot = df.pivot_table(
        index="State",
        columns="Category_Name",
        values="Total_Quantity",
        aggfunc="sum",
        fill_value=0,
    )
    df_pivot = df_pivot.reindex(df_state_sum["State"])
    ax = df_pivot.plot(kind="bar", stacked=True, figsize=(12, 7), colormap="tab20")

    plt.xlabel("State")
    plt.ylabel("Total Quantity")
    plt.title("Total Quantity by State and Category")
    plt.xticks(rotation=90)  # หมุนชื่อ State
    plt.tight_layout()  # จัดเรียงกราฟให้พอดี
    plt.legend(
        title="Category Name", bbox_to_anchor=(1.05, 1), loc="upper left"
    )  # ตั้งชื่อหมวดหมู่
    for container in ax.containers:
        ax.bar_label(
            container, label_type="center", fontsize=10, color="black", weight="bold"
        )

    plt.show()

    print("=" * 50)
