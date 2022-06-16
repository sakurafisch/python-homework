def main() -> None:
    i: int = 2
    while i <= 10:
        print(f"{i:>#2} + {i:>#2} = {i+i:>#2}")
        i += 2

if __name__ == "__main__":
    main()

# 张婷答案
# i = 1
# while i <= 5:
#     print("{0:>2} + {1:>2} = {2:>2}".format(2 * i, 2 * i, 2 * i + 2 * i))
#     i = i + 1
