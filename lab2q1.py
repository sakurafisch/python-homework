if __name__ == '__main__':
    number_of_item = int(input("Enter the number of items: "))
    print("")
    print("Receipt:")
    if (number_of_item <= 50):
        print(f"{number_of_item} items x $3 = ${number_of_item * 3}")
        print("Postage: $10")
        print(f"Total: ${number_of_item*3+10}")
    else:
        print(f"{number_of_item} items x $2 = ${number_of_item * 2}")
        print("Postage: free")
        print(f"Total: ${number_of_item*2}")
