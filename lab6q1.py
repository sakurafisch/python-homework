def main() -> None:
    number_list: list[int] = [1, 2, 3, 4, 1, 2, 3, 4]
    print(number_list)
    number_list.append(2000)
    print(number_list)
    number_list.remove(1)
    print(number_list)
    number_list[len(number_list) - 1] = 0
    print(number_list)
    number_list.insert(0, 1)
    print(number_list)
    number_list = [11, 12, 13, 14, 11, 12, 13, 14, 10]
    print(number_list)
    number_list = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    print(number_list)
    number_list = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    print(number_list)
    number_list.clear()
    print(number_list)

if __name__ == '__main__':
    main()
