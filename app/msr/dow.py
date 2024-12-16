from ...conn import create_connection, close_connection

import pandas as pd
import matplotlib.pyplot as plt

from prettytable import PrettyTable


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


def fetch_data_from_db(query):
    # Get data
    conn = create_connection()
    df = pd.read_sql(query, conn)
    close_connection(conn)

    return df


def plot_stacked_bar_chart():
    df = fetch_data_from_db(query)
    # Setting SubCategory_Name as the index
    df.set_index("SubCategory_Name", inplace=True)

    # Transpose the dataframe so we can plot by day of the week
    df_transposed = df.T

    # Create a stacked bar chart
    df_transposed.plot(kind="bar", stacked=True, figsize=(10, 6))

    # Set labels and title
    plt.title("Stacked Bar Chart of Amount by Days of Week")
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

    # Show plot
    plt.show()


if __name__ == "__main__":
    plot_stacked_bar_chart()
