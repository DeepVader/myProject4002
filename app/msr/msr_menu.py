MSR_listMenu = {
    "header": "Menu: Monthly Sales Reports: รายงานยอดขายรายเดือน",
    "1": "สรุปยอดขายรายวัน (จ.-อา.)",
    "2": "สรุปยอดขายรายสัปดาห์ (ตามรายการสินค้า)",
    "3": "สรุปยอดขายรายสัปดาห์ (ตามประเภทสินค้า)",
    "4": "สรุปยอดขายรายเดือน",
    "e": "Return to Data Analytics Menu",
}


def MSR_display():
    while True:
        from components.show_menu import show_menu

        show_menu(MSR_listMenu)
        print("=" * 50)
        choice = input("Please select a menu: ")
        print("=" * 50)

        if choice == "1":
            from msr.dailySalesR import plot_bar_chart

            print("Report: 7Day of Week")
            plot_bar_chart()
            # break
        elif choice == "2":
            from msr.subCat_weeklySalesR import display_paginated_table

            print("Report: SubCategory Weekly")
            display_paginated_table()
            break
        elif choice == "3":
            from msr.cat_weeklySalesR import plot_bar_chart

            print("Report: Category Weekly")
            plot_bar_chart()
            # break
        elif choice == "4":
            from msr.monthlySalesR import display_paginated_table

            print("Report: Monthly of Year")
            display_paginated_table()
            # break
        elif choice == "e":
            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()
            break
        else:
            print("Please try again.")
            print()