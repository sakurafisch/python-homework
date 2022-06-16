def bubbleSort(a_list: list):
    for passnum in range(len(a_list) - 1, 0, -1):
        for i in range(passnum):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

def ordered_sequential_search(a_list: list, item) -> tuple(bool, int):
    left: int = 0
    right: int = len(a_list) - 1;
    while (left <= right):
        mid: int = (left + right) // 2
        if item == a_list[mid]:
            return True, mid
        if item < a_list[mid]:
            right = mid - 1
            continue
        if item > a_list[mid]:
            left = mid + 1
    return False, -1

def sort_then_search (a_list: list, item):
    bubbleSort(a_list)
    return ordered_sequential_search(a_list, item)

def main() -> None:
    pass

if __name__ == "__main__":
    main()
