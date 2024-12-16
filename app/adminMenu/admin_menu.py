adminMenu_listMenu = {
    "header": "Menu: E-Commerce Data Analytics",
    "1": "Customer Details: ข้อมูลลูกค้า",
    "2": "Customer Purchase History: ประวัติการซื้อของลูกค้า",
    "3": "Monthly Sales Reports",
    "e": "Exit",
}


def adminMenu_display():
    while True:
        from components.show_menu import show_menu

        show_menu(adminMenu_listMenu)
        print("=" * 50)
        choice = input("Please select a menu: ")
        print("=" * 50)

        if choice == "1":
            # dayOfWeek()
            print("Menu: Customer Details")
            # break
        elif choice == "2":
            # weekly()
            print("Menu: Customer Purchase History")
            # break
        elif choice == "3":
            from msr.msr_menu import MSR_display

            MSR_display()
            break
        elif choice == "e":
            print()
            # print("End of program ...")
            print("End of program".center(50, " "))
            print("=" * 50)
            break
        else:
            print("Please try again.")
            print()
