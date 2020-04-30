random_list_of_nums = [5, 2, 1, 8, 4, -1, 0]


def bubleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # old = arr[i]
                #                 # arr[i] = arr[i + 1]
                #                 # arr[i+1] = old
                swapped = True

    return arr


print(bubleSort(random_list_of_nums))