def insertionSort(alist, order_boolean) -> None:
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        if order_boolean == True:
            while position > 0 and alist[position - 1] > currentvalue:
                alist[position] = alist[position - 1]
                position = position - 1
            alist[position] = currentvalue
            continue
        while position > 0 and alist[position - 1] < currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue

# 张婷答案
# def insertionSort(a_list, order_boolean):

#     if order_boolean is True:
#         for index in range(1, len(a_list)):
#             currentvalue = a_list[index]
#             position = index
#             while position > 0 and a_list[position - 1] > currentvalue:
#                 a_list[position] = a_list[position - 1]
#                 position = position - 1
#             a_list[position] = currentvalue
#     else:
#         for index in range(1, len(a_list)):
#             currentvalue = a_list[index]
#             position = index
#             while position > 0 and a_list[position - 1] < currentvalue:
#                 a_list[position] = a_list[position - 1]
#                 position = position - 1
#             a_list[position] = currentvalue