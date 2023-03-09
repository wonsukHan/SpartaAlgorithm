# input = [4, 6, 2, 9, 1]
#
#
# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return
#
#
# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
#
# input = [4, 6, 2, 9, 1]
#
#
# def selection_sort(array):
#     for i in range(len(array)):
#         min = i
#         for j in range(i + 1, len(array)):
#             if array[min] > array[j]:
#                 min = j
#         array[i], array[min] = array[min], array[i]
#     return
#
#
# selection_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
#
#
#
# input = [4, 6, 2, 9, 1]
#
#
# def insertion_sort(array):
#     for i in range(1, len(array)):
#         for j in range(i):
#             if array[i] < array[j]:
#                 array[i], array[j] = array[j], array[i]
#             else:
#                 break
#     return
#
#
# insertion_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array3 = []
    while len(array1) != 0 and len(array2) != 0:
        if array1[0] > array2[0]:
            array3.append(array2[0])
            array2 = array2[1:]
        elif array1[0] < array2[0]:
            array3.append(array1[0])
            array1 = array1[1:]
        if len(array1) == 0:
            array3 += array2
        if len(array2) == 0:
            array3 += array1
    return array3


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) == 1:
        return array
    return merge(merge_sort(array[:len(array)//2]), merge_sort(array[len(array)//2:]))


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
