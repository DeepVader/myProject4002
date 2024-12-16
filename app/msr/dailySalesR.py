import matplotlib.pyplot as plt


query = """SELECT SubCategories.SubCategory_Name,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Monday' THEN OrderDetails.Amount ELSE 0 END) AS Monday,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Tuesday' THEN OrderDetails.Amount ELSE 0 END) AS Tuesday,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Wednesday' THEN OrderDetails.Amount ELSE 0 END) AS Wednesday,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Thursday' THEN OrderDetails.Amount ELSE 0 END) AS Thursday,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Friday' THEN OrderDetails.Amount ELSE 0 END) AS Friday,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Saturday' THEN OrderDetails.Amount ELSE 0 END) AS Saturday,
        SUM(CASE WHEN DAYNAME(Orders.Order_Date) = 'Sunday' THEN OrderDetails.Amount ELSE 0 END) AS Sunday
    FROM ecommerce.OrderDetails
    JOIN ecommerce.Orders ON OrderDetails.Order_ID = Orders.Order_ID
    JOIN ecommerce.SubCategories ON OrderDetails.SubCategory_ID = SubCategories.SubCategory_ID
    GROUP BY OrderDetails.SubCategory_ID
    ORDER BY OrderDetails.SubCategory_ID;
    """


def plot_bar_chart():
    from db.get import pd_readSQL_fromDB

    df = pd_readSQL_fromDB(query)
    df.set_index("SubCategory_Name", inplace=True)

    df_transposed = df.T

    df_transposed.plot(kind="bar", stacked=True, figsize=(10, 6))

    plt.title("Bar Chart of Amount by Days of Week")
    plt.xlabel("Days of Week")
    plt.ylabel("Amount")
    plt.xticks(rotation=0)

    plt.legend(
        loc="upper left",
        bbox_to_anchor=(1, 1),
        title="SubCategory",
        fontsize=10,
        title_fontsize=12,
    )

    plt.show()
