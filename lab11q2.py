def binary_search(a_list, item, start=0):
    if len(a_list) == 0:
        return False, -1
    mid = len(a_list) // 2
    print(f"A comparison of {item} and the element at index {start+mid}")
    if a_list[mid] == item:
        return True, start+mid
    if item > a_list[mid]:
        return binary_search(a_list[:mid], item, start)
    if item < a_list[mid]:
        return binary_search(a_list[(mid+1):], item, start = start+mid+1)
