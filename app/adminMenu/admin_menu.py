adminMenu_listMenu = {
    "header": "Menu: E-Commerce Data Analytics",
    "1": "Customer Details",
    "2": "Purchase History",
    "3": "Monthly Sales Reports",
    "4": "Manage Items",
    "5": "Backup",
    "e": "Exit",
}


def adminMenu_display():
    while True:
        from components.show_menu import show_menu

        show_menu(adminMenu_listMenu)
        print("=" * 50)
        choice = input("Please select a menu: ")
        print()

        if choice == "1":
            from Demo_CS.Demo_CS import Customer_detail

            Customer_detail()
            break

        elif choice == "2":
            from purchase_history.ph_menu import ph_display

            ph_display()
            break

        elif choice == "3":
            from msr.msr_menu import MSR_display

            MSR_display()
            break

        elif choice == "4":
            from crud.category_menu import manage_categories

            manage_categories()
            break

        elif choice == "5":
            from backup.backup import backup_db

            backup_db()
            break

        elif choice == "e":
            print("End of program".center(50, " "))
            print("=" * 50)
            break

        else:
            print("Please try again.")
            print()
