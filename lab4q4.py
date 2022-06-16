def next_number(x: int) -> int:
    if x % 2 == 0:
        return 3 * x + 1
    return 2 * x + 2

def main() -> None:
    x: int = int(input('Enter the initial number: '))
    print('Sequence:')
    count: int = 0
    while x <= 100:
        print(f'Step {count}: {x}')
        count += 1
        x = next_number(x)
    print(f'Step {count}: {x}')

if __name__ == '__main__':
    main()
