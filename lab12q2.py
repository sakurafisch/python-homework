def selectionSort_descending_order(a_list):
    for fillslot in range(len(a_list) - 1, 0, -1):
        positionOfMax: int = 0
        for location in range(1, fillslot + 1):
            if a_list[location] < a_list[positionOfMax]:
                positionOfMax = location
        temp = a_list[fillslot]
        a_list[fillslot] = a_list[positionOfMax]
        a_list[positionOfMax] = temp    

def main() -> None:
    pass

if __name__ == "__main__":
    main()