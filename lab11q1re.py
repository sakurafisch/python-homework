def ordered_sequential_search(a_list, item):
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

