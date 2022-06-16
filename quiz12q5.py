def ordered_sequential_search_descending_order(a_list, item, start = 0):
# add your code here
    if len(a_list) == 0:
        return False, -1
    mid: int = len(a_list) // 2
    if a_list[mid] == item:
        return True, start + mid
    if item > a_list[mid]:
        return ordered_sequential_search_descending_order(a_list[:mid], item, start)
    if item < a_list[mid]:
        return ordered_sequential_search_descending_order(a_list[(mid+1):], item, start = start+mid+1)

# def ordered_sequential_search(a_list, item, start = 0):
#     if len(a_list) == 0:
#         return False, -1
#     mid: int = len(a_list) // 2
#     if a_list[mid] == item:
#         return True, start + mid
#     if item < a_list[mid]:
#         return ordered_sequential_search(a_list[:mid], item, start)
#     if item > a_list[mid]:
#         return ordered_sequential_search(a_list[(mid+1):], item, start = start+mid+1)


def bubbleSort_descending_order(a_list):
# sorts the list in descending order 
# add your code here
    for passnum in range(len(a_list) - 1, 0, -1):
        for i in range(passnum):
            if a_list[i] < a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

def sort_then_search(a_list, item):
# add your code here
    bubbleSort_descending_order(a_list)
    return ordered_sequential_search_descending_order(a_list, item)