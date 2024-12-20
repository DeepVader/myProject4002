def show_customer_data():
    from db.get import fetch_data
    from components.displayTable import display_table

    customer_name = input("Please enter the Customer Name: ").strip()
    query = """
        SELECT c.Customer_Name, o.Order_ID, o.Order_Date, od.Amount, od.Quantity, 
               cat.Category_Name, subcat.SubCategory_Name
        FROM Customers c
        JOIN Orders o ON c.Customer_ID = o.Customer_ID
        JOIN OrderDetails od ON o.Order_ID = od.Order_ID
        JOIN SubCategories subcat ON od.SubCategory_ID = subcat.SubCategory_ID
        JOIN Categories cat ON subcat.Category_ID = cat.Category_ID
        WHERE LOWER(c.Customer_Name) = LOWER(%s)
        ORDER BY o.Order_ID;
    """
    data = fetch_data(query, (customer_name,))

    if not data:
        print(f"\nNo data found for customer: {customer_name}")
        return

    total_amount = sum(row[3] for row in data)
    total_quantity = sum(row[4] for row in data)

    print("=" * 50)
    print(("Purchase Report for " + customer_name).center(50, " "))
    print("=" * 50)
    print(f"Total Amount: {total_amount:.2f}")
    print(f"Total Quantity: {total_quantity}\n")

    # แสดงตารางข้อมูล
    display_table(
        [
            "Customer Name",
            "Order ID",
            "Order Date",
            "Amount",
            "Quantity",
            "Category",
            "SubCategory",
        ],
        data,
    )

    from purchase_history.ph_menu import ph_display

    ph_display()
