def show_menu(menu):
    # Display the header if it exists
    if "header" in menu:
        print(menu["header"].center(50, " "))  # Center the header with padding
        print("=" * 50)

    # Display menu options, excluding "header" and "e"
    for key in sorted(menu.keys()):
        if key not in ["header", "e"]:
            print(f"{key}. {menu[key]}")  # Print menu options

    # Display the "e" option if it exists
    if "e" in menu:
        print()  # Add space before "e" option
        print(f"e. {menu['e']}")  # Print the "e" option to exit
    print()  # Final newline for clarity
