def quickSort_descending_order(a_list) -> None:
    quickSortHelper(a_list, 0, len(a_list) - 1)

def quickSortHelper(a_list, first, last) -> None:
    if first < last:
        splitpoint = partition(a_list, first, last)
        quickSortHelper(a_list, first, splitpoint - 1)
        quickSortHelper(a_list, splitpoint + 1, last)

def partition(a_list, first, last) -> int:
    pivotvalue = a_list[first]
    leftmark = first + 1
    rightmark = last
    while True:
        while leftmark <= rightmark and a_list[leftmark] >= pivotvalue:
            leftmark = leftmark + 1
        while a_list[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            break
        temp = a_list[leftmark]
        a_list[leftmark] = a_list[rightmark]
        a_list[rightmark] = temp
    temp = a_list[first]
    a_list[first] = a_list[rightmark]
    a_list[rightmark] = temp
    return rightmark

def main() -> None:
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort_descending_order(a_list)
    print(a_list)

if __name__ == '__main__':
    main()
