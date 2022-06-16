def generate_list(t: int) -> list:
    l: list[int] = []
    for i in range(0, t):
        l.append(pow(i, 2))
    return l

def print_list(l: list) -> None:
    print(f'Here is a list of generated squares: {l}')

def main() -> None:
    t: int = int(input('How many square numbers to generate? '))
    l: list = generate_list(t)
    print_list(l)

if __name__ == '__main__':
    main()
