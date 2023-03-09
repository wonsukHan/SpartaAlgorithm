finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    while len(array) != 1:
        if array[len(array)//2] > target:
            array = array[:len(array)//2]
        elif array[len(array)//2] < target:
            array = array[len(array)//2:]
        elif array[len(array)//2] == target:
            return True
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()
    while len(array) != 1:
        if array[len(array) // 2] > target:
            array = array[:len(array) // 2]
        elif array[len(array) // 2] < target:
            array = array[len(array) // 2:]
        elif array[len(array) // 2] == target:
            return True
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)