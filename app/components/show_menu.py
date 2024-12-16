def show_menu(menu):
    # ถ้ามี "header" ให้แสดง header ก่อน
    if "header" in menu:
        print(menu["header"].center(50, " "))
        print("=" * 50)

    # แสดงเมนูตัวเลือกที่ไม่ใช่ "header" และ "e"
    for key in sorted(menu.keys()):
        if key != "header" and key != "e":
            print(f"{key}. {menu[key]}")

    # แสดง "e" ที่ด้านล่างสุด (ถ้ามี)
    if "e" in menu:
        print()
        print(f"e. {menu['e']}")
    print()
