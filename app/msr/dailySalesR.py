import matplotlib.pyplot as plt
import pandas as pd


query = """
SELECT SubCategories.SubCategory_Name,
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


def plot_sales_by_day():
    from db.get import fetch_data_from_db

    rows, columns = fetch_data_from_db(query)

    if rows is None or columns is None:
        print("No data available.")
        return

    df = pd.DataFrame(rows, columns=columns)

    df.set_index("SubCategory_Name", inplace=True)
    df = df.apply(pd.to_numeric)

    sales_data_transposed = df.T

    sales_data_transposed.plot(kind="bar", stacked=True, figsize=(10, 6))

    plt.title("Sales by Day of Week")
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

    plt.tight_layout()

    plt.show()
