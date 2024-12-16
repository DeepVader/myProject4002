from prettytable import PrettyTable


query = """SELECT SubCategories.SubCategory_Name,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 1 THEN OrderDetails.Amount ELSE 0 END) AS January,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 2 THEN OrderDetails.Amount ELSE 0 END) AS February,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 3 THEN OrderDetails.Amount ELSE 0 END) AS March,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 4 THEN OrderDetails.Amount ELSE 0 END) AS April,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 5 THEN OrderDetails.Amount ELSE 0 END) AS May,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 6 THEN OrderDetails.Amount ELSE 0 END) AS June,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 7 THEN OrderDetails.Amount ELSE 0 END) AS July,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 8 THEN OrderDetails.Amount ELSE 0 END) AS August,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 9 THEN OrderDetails.Amount ELSE 0 END) AS September,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 10 THEN OrderDetails.Amount ELSE 0 END) AS October,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 11 THEN OrderDetails.Amount ELSE 0 END) AS November,
    SUM(CASE WHEN MONTH(Orders.Order_Date) = 12 THEN OrderDetails.Amount ELSE 0 END) AS December
FROM ecommerce.OrderDetails
JOIN ecommerce.Orders ON OrderDetails.Order_ID = Orders.Order_ID
JOIN ecommerce.SubCategories ON OrderDetails.SubCategory_ID = SubCategories.SubCategory_ID
GROUP BY SubCategories.SubCategory_Name
ORDER BY SubCategories.SubCategory_Name;
"""


def display_paginated_table():
    from db.get import pd_readSQL_fromDB

    df = pd_readSQL_fromDB(query)
    df.set_index("SubCategory_Name", inplace=True)
    df_transposed = df.T

    table = PrettyTable()
    table.field_names = ["Month"] + df_transposed.columns.tolist()

    for row in df_transposed.itertuples():
        row_data = list(row)
        if row_data[0] in [
            "January",
            "March",
            "August",
            "September",
            "October",
            "November",
        ]:
            row_data[0] = f"**{row_data[0]}**"
        table.add_row(row_data)

    print(table)
