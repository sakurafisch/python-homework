def quickSort(alist, order) -> None:
    quickSortHelper(alist, 0, len(alist) - 1, order)

def quickSortHelper(alist, first, last, order) -> None:
    if first < last:
        splitpoint = partition(alist, first, last, order)
        quickSortHelper(alist, first, splitpoint - 1, order)
        quickSortHelper(alist, splitpoint + 1, last, order)

def partition(alist, first, last, order) -> int:
    if order:
        pivotvalue = alist[first]
        leftmark = first + 1
        rightmark = last
        while True:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1
            if rightmark < leftmark:
                break
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        return rightmark
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    while True:
        while leftmark <= rightmark and alist[leftmark] >= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            break
        temp = alist[leftmark]
        alist[leftmark] = alist[rightmark]
        alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
