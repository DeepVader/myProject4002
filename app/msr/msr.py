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
        print("=" * 30)
        choice = input("Please select a menu: ")
        print("=" * 30)

        if choice == "1":
            # dayOfWeek()
            print("Report: 7Day of Week")
            # break
        elif choice == "2":
            # weekly()
            print("Reports: SubCat Weekly of Year")
            # break
        elif choice == "3":
            # monthlyReport()
            print("Reports: Cat Weekly of Year")
            # break
        elif choice == "4":
            # monthlyReport()
            print("Reports: Monthly of Year")
            # break
        elif choice == "e":
            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()
            break
        else:
            print("Please try again.")
            print()
