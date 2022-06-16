if __name__ == '__main__':
    number_of_items = int(input("Enter the number of items: "))
    shipping_method = input("Enter shipping method (s/r/e): ")
    print("")
    print("Receipt:")
    if number_of_items <= 50:
        sum = number_of_items * 3
        print(f"{number_of_items} items x $3 = ${sum}")
        if (shipping_method == 's'):
            print("Stanard post: $10")
            sum += 10
        elif (shipping_method == 'r'):
            print("Postage: $15")
            sum += 15
        elif (shipping_method == 'e'):
            print("Express post: $20")
            sum += 20
        print(f"Total: ${sum}")
    else:
        sum = number_of_items * 2
        print(f"{number_of_items} items x $2 = ${sum}")
        if (shipping_method == 's'):
            print("Standard post: free")
        elif (shipping_method == 'r'):
            print("Registered post: $10")
            sum += 10
        elif (shipping_method == 'e'):
            print("Express post: $17")
            sum += 17
        print(f"Total: ${sum}")
