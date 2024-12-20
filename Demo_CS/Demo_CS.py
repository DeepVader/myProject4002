demoCS_listMenu = {
    "header": "Menu: Customer Detail",
    "1": "Customer Segmentation",
    "2": "Customer Purchase Behavior",
    "3": "Demographic Trends",
    "e": "Return to Data Analytics Menu",
}


def Customer_detail():
    while True:
        from components.show_menu import show_menu

        # Display the MSR menu
        show_menu(demoCS_listMenu)
        print("=" * 50)
        choice = input("Please select a menu: ")
        print()

        if choice == "1":
            from Demo_CS.cs_segment import Customer_Segment

            Customer_Segment()

        elif choice == "2":
            from Demo_CS.cs_purchase import Customer_Purchase

            Customer_Purchase()

        elif choice == "3":
            from Demo_CS.cs_demographic import Demographic_Trends

            Demographic_Trends()

        elif choice == "e":
            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()  # กลับไปเมนูหลัก
            break

        else:
            print("Please try again.")
            print()
