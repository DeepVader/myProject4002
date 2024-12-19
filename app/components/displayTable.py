import pandas as pd
from prettytable import PrettyTable


def display_table_catID(rows, columns, txt=None):
    if rows is None or columns is None:
        print("Error!".center(50, " "))
        print("=" * 50)
        print("No data available.")
        print()

    else:
        df = pd.DataFrame(rows, columns=columns)
        df.set_index("Category_ID", inplace=True)

        table = PrettyTable()
        table.field_names = ["Category_ID"] + df.columns.tolist()

        for row in df.itertuples():
            table.add_row(row)

        if txt is not None:
            print(txt.center(50, " "))
            print("=" * 50)
        else:
            pass
        print(table)


def display_table(columns, data, title=None):
    table = PrettyTable()
    table.field_names = columns
    for row in data:
        table.add_row(row)
    if title:
        print(f"\n===== {title} =====")
    print(table)
