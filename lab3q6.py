if __name__ == '__main__':
    count: int = 0
    sum: int = 0
    even: int = 0
    odd: int = 0
    positive: int = 0
    negative: int = 0
    input_str : str = input("Enter an integer or q to quit: ")
    while (input_str != 'q'):
        input_int : int = int(input_str)
        sum += input_int
        if input_int % 2 == 0:
            even += 1
        else:
            odd += 1
        if input_int > 0:
            positive += 1
        elif input_int < 0:
            negative += 1
        count += 1
        input_str = input("Enter an integer or q to quit: ")
    print("")
    print("Summary information:")
    print(f"You have entered {count} integers.")
    print(f"The sum of these numbers is {sum}.")
    print(f"There are {even} even numbers.")
    print(f"There are {odd} odd numbers.")
    print(f"There are {positive} positive numbers.")
    print(f"There are {negative} negative numbers.")

# 张婷答案
# even_count = 0
# odd_count = 0
# int_count = 0
# sum_result = 0
# positive_count = 0
# negative_count = 0
# while True:
#     user_input = input("Enter an integer or q to quit: ")
#     if user_input == "q":
#         break
#     number = int(user_input)
#     int_count += 1
#     sum_result = sum_result + number
#     if number > 0:
#         positive_count += 1
#     elif number < 0:
#         negative_count += 1
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print()
# print("Summary information:")
# print("You have entered {0} integers.".format(int_count))
# print("The sum of these numbers is {0}.".format(sum_result))
# print("There are {} even numbers.".format(even_count))
# print("There are {} odd numbers.".format(odd_count))
# print("There are {} positive numbers.".format(positive_count))
# print("There are {} negative numbers.".format(negative_count))
