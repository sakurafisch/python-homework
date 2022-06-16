def triple(sentence: str) -> str:
    ans: str = ''
    i: int = 0
    while i < len(sentence):
        ans += sentence[i] * 3
        i += 1
    return ans

def main() -> None:
    sentence: str = input('Enter a sentence: ')
    print(f'Triple effect: {triple(sentence)}')

if __name__ =='__main__':
    main()
