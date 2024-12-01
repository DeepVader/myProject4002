from purhis import purHis


def menuShop(data):
    c_data = data
    print("=" * 50)
    print(c_data[1])
    print("=" * 50)
    print("Menu")
    print("1: his")
    print("2: shop")
    print("3: back to menu")

    # input
    choice = input("Select: ")

    if choice == "1":
        print("1")
        purHis(c_data)
    elif choice == "2":
        print("2")
    elif choice == "3":
        print("3")
    else:
        print("exit")


if __name__ == "__main__":
    result = (0, 0, 0, 0)
    menuShop(result)
