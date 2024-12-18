from prettytable import PrettyTable
import pandas as pd

from db.get import get_max_week

max_weeks = get_max_week()
query = "SELECT SubCategories.SubCategory_Name"
for week in range(1, max_weeks + 1):
    query += f", SUM(CASE WHEN WEEK(Orders.Order_Date) = {week} THEN OrderDetails.Amount ELSE 0 END) AS Week_{week}"
query += """
FROM ecommerce.OrderDetails
JOIN ecommerce.Orders ON OrderDetails.Order_ID = Orders.Order_ID
JOIN ecommerce.SubCategories ON OrderDetails.SubCategory_ID = SubCategories.SubCategory_ID
GROUP BY SubCategories.SubCategory_Name
ORDER BY SubCategories.SubCategory_Name;
"""


def display_paginated_table():
    from db.get import fetch_data_from_db

    rows, columns = fetch_data_from_db(query)

    if rows is None or columns is None:
        print("No data available.")
        return

    df = pd.DataFrame(rows, columns=columns)

    df.set_index("SubCategory_Name", inplace=True)
    df = df.apply(pd.to_numeric)

    df_transposed = df.T

    rows_per_page = 10

    total_pages = (len(df_transposed) // rows_per_page) + (
        1 if len(df_transposed) % rows_per_page != 0 else 0
    )

    current_page = 1

    while True:
        start_row = (current_page - 1) * rows_per_page
        end_row = start_row + rows_per_page
        current_data = df_transposed.iloc[start_row:end_row]

        table = PrettyTable()
        table.field_names = ["Week"] + current_data.columns.tolist()

        for idx, row in current_data.iterrows():
            table.add_row([idx] + row.tolist())

        print(f"\nPage {current_page} of {total_pages}")
        print(table)
        print("\n" + "-" * 50)
        print("\nOptions: [N]ext, [P]revious, [Q]uit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == "n" and current_page < total_pages:
            current_page += 1
        elif choice == "p" and current_page > 1:
            current_page -= 1
        elif choice == "q":
            from msr.msr_menu import MSR_display

            MSR_display()
            break
        else:
            print("Invalid choice, try again.")
