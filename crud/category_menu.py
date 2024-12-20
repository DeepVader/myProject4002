def manage_categories():
    while True:
        print("Menu: Manage Categories".center(50, " "))
        print("=" * 50)
        from crud.category_func import read_all_categories

        read_all_categories()
        print("Options: [C]reate, [U]pdate, [D]elete, [Q]uit")
        print()

        print("=" * 50)
        choice = input("Enter your choice: ").strip().lower()
        print()

        if choice == "c":
            from crud.category_func import create_category

            create_category()
            break

        elif choice == "u":
            from crud.category_func import edit_category

            edit_category()
            break

        elif choice == "d":
            from crud.category_func import delete_category

            delete_category()
            break

        elif choice == "q":
            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()
            break

        else:
            print("Please try again.")
            print()
