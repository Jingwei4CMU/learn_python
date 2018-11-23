#  fib dic

# fib_dic = {0:0,1:1}
# def get_fib(position):
#     try:
#         return fib_dic[position]
#     except:
#         result =  get_fib(position-2) + get_fib(position-1)
#         fib_dic[position] = result
#         return result
#
# # Test cases
# print (get_fib(300))
# print (get_fib(11))
# print (get_fib(0))
#
# list=[1,2,3,4,5]
# print()




# quick sort


#
# def issorted(array):
#     for i in range(len(array)):
#         if i == 0:
#             continue
#         if array[i - 1] <= array[i]:
#             continue
#         else:
#             return False
#     return True
#
#
# def quicksort(array):
#     print('now sort:',array)
#     if issorted(array):
#         return array
#     pivot_index = len(array) - 1
#     start_index = 0
#     while start_index != pivot_index:
#         if array[pivot_index] <= array[start_index]:
#             if pivot_index - start_index > 1:
#                 temp = array[start_index]
#                 array[start_index] = array[pivot_index - 1]
#                 array[pivot_index - 1] = array[pivot_index]
#                 array[pivot_index] = temp
#                 pivot_index = pivot_index - 1
#             else:
#                 temp = array[start_index]
#                 array[start_index] = array[pivot_index]
#                 array[pivot_index] = temp
#                 pivot_index = pivot_index - 1
#         else:
#             start_index = start_index + 1
#     # print(pivot_index)
#     if pivot_index == 0:
#         return array[pivot_index] + quicksort(array[pivot_index+1:])
#     elif pivot_index == len(array)-1:
#         return quicksort(array[:pivot_index]) + [array[pivot_index]]
#     else:
#         return quicksort(array[:pivot_index]) + [array[pivot_index]] + quicksort(array[pivot_index+1:])
#
#
#
# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# print(quicksort(test))
