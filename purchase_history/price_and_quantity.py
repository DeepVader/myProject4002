import matplotlib.pyplot as plt


def show_sum_price_and_quantity():
    from db.get import fetch_data
    from components.displayTable import display_table

    categories_query = """
        SELECT c.Category_Name, 
               SUM(od.Amount) AS Total_Price, 
               SUM(od.Quantity) AS Total_Quantity,
               AVG(od.Amount / od.Quantity) AS Avg_Price,
               (SUM(od.Amount) / SUM(SUM(od.Amount)) OVER()) * 100 AS Percentage
        FROM Categories c
        JOIN SubCategories sc ON c.Category_ID = sc.Category_ID
        JOIN OrderDetails od ON sc.SubCategory_ID = od.SubCategory_ID
        GROUP BY c.Category_Name;
    """
    categories_data = fetch_data(categories_query)

    subcategories_query = """
        SELECT sc.SubCategory_Name, 
               SUM(od.Amount) AS Total_Price, 
               SUM(od.Quantity) AS Total_Quantity,
               AVG(od.Amount / od.Quantity) AS Avg_Price,
               (SUM(od.Amount) / SUM(SUM(od.Amount)) OVER()) * 100 AS Percentage
        FROM SubCategories sc
        JOIN OrderDetails od ON sc.SubCategory_ID = od.SubCategory_ID
        GROUP BY sc.SubCategory_Name;
    """
    subcategories_data = fetch_data(subcategories_query)

    # แสดงหัวข้อและข้อมูลรวม
    print("=" * 50)
    print("Total Sales and Quantity Summary".center(50, " "))
    print("=" * 50)

    # แสดงตารางข้อมูล
    print("\nTotal Price by Category:")
    display_table(
        [
            "Category Name",
            "Total Price",
            "Total Quantity",
            "Average Price",
            "Percentage (%)",
        ],
        categories_data,
    )

    print("\nTotal Price by SubCategory:")
    display_table(
        [
            "SubCategory Name",
            "Total Price",
            "Total Quantity",
            "Average Price",
            "Percentage (%)",
        ],
        subcategories_data,
    )

    # เตรียมข้อมูลกราฟ
    categories = [row[0] for row in categories_data]
    total_prices_categories = [row[1] for row in categories_data]
    total_quantities_categories = [row[2] for row in categories_data]

    subcategories = [row[0] for row in subcategories_data]
    total_prices_subcategories = [row[1] for row in subcategories_data]
    total_quantities_subcategories = [row[2] for row in subcategories_data]

    # กราฟ
    plt.figure(figsize=(10, 5))
    plt.bar(categories, total_prices_categories, color="blue")
    plt.title("Total Price by Categories")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(subcategories, total_prices_subcategories, color="green")
    plt.title("Total Price by SubCategories")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(categories, total_quantities_categories, color="orange")
    plt.title("Total Quantity by Categories")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(subcategories, total_quantities_subcategories, color="red")
    plt.title("Total Quantity by SubCategories")
    plt.xticks(rotation=45)
    plt.show()
