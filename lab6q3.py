def main() -> None:
    l: list[int] = []
    while True:
        inp: str = input('Enter an integer (enter QUIT to quit): ')
        if inp == "QUIT":
            break
        l.append(int(inp))
    print(f"You have entered: {l}")

if __name__ == '__main__':
    main()
