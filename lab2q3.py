def min(x: int, y: int) -> int:
    if (x < y):
        return x
    else:
        return y

def max(x: int, y: int) -> int:
    if (x > y):
        return x
    else:
        return y

if __name__ == '__main__':
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))
    third = int(input("Enter the third integer: "))
    fourth = int(input("Enter the fourth integer: "))
    print("")
    mi = min(min(first, second), min(third, fourth))
    ma = max(max(first, second), max(third, fourth))
    print(f"The minimum number is {mi} and the maximum number is {ma}.")
