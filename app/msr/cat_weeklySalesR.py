import matplotlib.pyplot as plt


from db.get import get_maxWeek_fromDB

max_weeks = get_maxWeek_fromDB()


query = "SELECT Categories.Category_Name"
for week in range(1, max_weeks + 1):
    query += f", SUM(CASE WHEN WEEK(Orders.Order_Date) = {week} THEN OrderDetails.Amount ELSE 0 END) AS Week_{week}"

query += """
FROM ecommerce.OrderDetails
JOIN ecommerce.Orders ON OrderDetails.Order_ID = Orders.Order_ID
JOIN ecommerce.SubCategories ON OrderDetails.SubCategory_ID = SubCategories.SubCategory_ID
JOIN ecommerce.Categories ON SubCategories.Category_ID = Categories.Category_ID
GROUP BY Categories.Category_Name
ORDER BY Categories.Category_Name;
"""


def plot_bar_chart():
    from db.get import pd_readSQL_fromDB

    df = pd_readSQL_fromDB(query)
    df.set_index("Category_Name", inplace=True)
    df_transposed = df.T

    df_transposed.plot(kind="bar", stacked=True, figsize=(10, 6))

    plt.title("Bar Chart of Amount by Weekly")
    plt.xlabel("Weekly")
    plt.ylabel("Amount")

    plt.legend(
        loc="upper left",
        bbox_to_anchor=(1, 1),
        title="Category",
        fontsize=10,
        title_fontsize=12,
    )

    plt.show()
