ph_listMenu = {
    "header": "Menu: Purchase History",
    "1": "View Total Sales and Quantity Summary",
    "2": "View Total Purchase Report",
    "3": "Search by Customer Name",
    "e": "Return to Data Analytics Menu",
}


def ph_display():
    while True:
        from components.show_menu import show_menu

        # Display the MSR menu
        show_menu(ph_listMenu)
        print("=" * 50)
        choice = input("Please select a menu: ")
        print()

        if choice == "1":
            from purchase_history.price_and_quantity import show_sum_price_and_quantity

            show_sum_price_and_quantity()

        elif choice == "2":
            from purchase_history.total_purchase import show_total_purchase

            show_total_purchase()
            break

        elif choice == "3":
            from purchase_history.customer_data import show_customer_data

            show_customer_data()
            break

        elif choice == "e":
            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()
            break

        else:
            print("Please try again.")
            print()
