def mergeSort_descending_order(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]
        mergeSort_descending_order(lefthalf)
        mergeSort_descending_order(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]:
                a_list[k] = lefthalf[i]
                i = i + 1
            else:
                a_list[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            a_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            a_list[k] = righthalf[j]
            j = j + 1
            k = k + 1

#张婷答案
# def mergeSort_descending_order(a_list):
#     #print("Splitting ", a_list)
#     if len(a_list) > 1:
#         mid = len(a_list)//2
#         lefthalf = a_list[:mid]
#         righthalf = a_list[mid:]
#         mergeSort_descending_order(lefthalf)
#         mergeSort_descending_order(righthalf)
#         i = 0
#         j = 0
#         k = 0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] >= righthalf[j]:
#                 a_list[k] = lefthalf[i]
#                 i = i + 1
#             else:
#                 a_list[k] = righthalf[j]
#                 j = j + 1
#             k = k + 1
#         while i < len(lefthalf):
#             a_list[k] = lefthalf[i]
#             i = i + 1
#             k = k + 1
#         while j < len(righthalf):
#             a_list[k] = righthalf[j]
#             j = j + 1
#             k = k + 1
