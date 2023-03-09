input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    ans = -1
    for i in range(len(array)):
        if ans == -1:
            ans = array[i]
        else:
            if ans * array[i] > ans + array[i]:
                ans = ans * array[i]
            elif ans * array[i] < ans + array[i]:
                ans = ans + array[i]
    return ans


result = find_max_plus_or_multiply(input)
print(result)