def show_total_purchase():
    from db.get import fetch_data
    from components.displayTable import display_table

    query = """
        SELECT c.Customer_Name, o.Order_ID, o.Order_Date, od.Amount, od.Quantity, 
               cat.Category_Name, subcat.SubCategory_Name
        FROM Customers c
        JOIN Orders o ON c.Customer_ID = o.Customer_ID
        JOIN OrderDetails od ON o.Order_ID = od.Order_ID
        JOIN SubCategories subcat ON od.SubCategory_ID = subcat.SubCategory_ID
        JOIN Categories cat ON subcat.Category_ID = cat.Category_ID
        ORDER BY o.Order_ID;
    """
    data = fetch_data(query)

    total_amount = sum(row[3] for row in data)
    total_quantity = sum(row[4] for row in data)

    # แสดงหัวข้อและข้อมูลรวม
    print("=" * 50)
    print("Total Purchase Report".center(50, " "))
    print("=" * 50)
    print(f"Total Amount: {total_amount:.2f}")
    print(f"Total Quantity: {total_quantity}\n")

    rows_per_page = 25  # แสดง 25 รายการต่อหน้า
    total_pages = (len(data) // rows_per_page) + (
        1 if len(data) % rows_per_page != 0 else 0
    )

    current_page = 1

    while True:
        start_row = (current_page - 1) * rows_per_page
        end_row = start_row + rows_per_page
        current_data = data[start_row:end_row]

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
            current_data,
        )

        print(f"\nPage {current_page} of {total_pages}")
        print("\n" + "-" * 50)
        print("\nOptions: [N]ext, [P]revious, [Q]uit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == "n" and current_page < total_pages:
            current_page += 1
        elif choice == "p" and current_page > 1:
            current_page -= 1
        elif choice == "q":
            from purchase_history.ph_menu import ph_display

            ph_display()
            break
        else:
            print("Invalid choice, try again.")
