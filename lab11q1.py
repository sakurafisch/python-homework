def ordered_sequential_search(a_list, item, start = 0):
    if len(a_list) == 0:
        return False, -1
    mid: int = len(a_list) // 2
    if a_list[mid] == item:
        return True, start + mid
    if item < a_list[mid]:
        return ordered_sequential_search(a_list[:mid], item, start)
    if item > a_list[mid]:
        return ordered_sequential_search(a_list[(mid+1):], item, start = start+mid+1)

# 张婷答案
# def ordered_sequential_search(a_list: list, item):
#     for i in range(0, len(a_list)):
#         if a_list[i] > item:
#             return False, -1
#         if a_list[i] == item:
#             return True, i

