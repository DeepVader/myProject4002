def read_all_categories():
    from db.crud_category import read_all_cat_from_db

    rows, columns = read_all_cat_from_db()
    from components.crud_display import display_table_catID

    display_table_catID(rows, columns)


def create_category():
    print("[C]reate Category".center(50, " "))
    print("=" * 50)
    name = input("Enter category name: ")
    print()

    from db.crud_category import create_one_cat_from_db

    val = (name,)
    rows, columns = create_one_cat_from_db(val)
    from components.crud_display import display_table_catID

    txt = "New Category"
    display_table_catID(rows, columns, txt)

    from crud.category_menu import manage_categories

    manage_categories()


def edit_category():
    print("[U]pdate Category Name".center(50, " "))
    print("=" * 50)
    id = input("Enter category ID")
    new_name = input("Enter category name: ")
    print()

    from db.crud_category import edit_one_cat_from_db

    val = (
        new_name,
        id,
    )
    rows, columns = edit_one_cat_from_db(val)
    from components.crud_display import display_table_catID

    txt = "Category Name Updated"
    display_table_catID(rows, columns, txt)

    from crud.category_menu import manage_categories

    manage_categories()


def delete_category():
    print("[D]elete Category ID".center(50, " "))
    print("=" * 50)
    id = input("Enter category ID")
    print()

    while True:
        print(f"Do you want to delete the category ID: {id}?")
        print("\nOptions: [Y]es, [N]o")
        choice = input("Enter your choice: ").strip().lower()
        print()

        if choice == "y":
            from db.crud_category import delete_one_cat_from_db

            val = (id,)
            rows, columns = delete_one_cat_from_db(val)
            from components.crud_display import display_table_catID

            txt = f"Category ID:{id} Deleted"
            display_table_catID(rows, columns, txt)

            from crud.category_menu import manage_categories

            manage_categories()
            break

        elif choice == "n":
            from crud.category_menu import manage_categories

            manage_categories()
            break

        else:
            print("Please try again.")
            print()
