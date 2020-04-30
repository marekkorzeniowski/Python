
def partion (numbs, low, high):

    pivot = numbs[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while numbs[i] < pivot:
            i += 1

        j -= 1
        while numbs[j] > pivot:
            j -= 1

        if i >= j:
            return j

        numbs[i], numbs[j] = numbs[j], numbs[i]


def quickSort(numbs):

    def _quicksort(items, low, high):
        if low < high:
            split_index = partion(numbs, low, high)
            _quicksort(items, low, split_index)
            _quicksort(items, split_index + 1, high)

    _quicksort(numbs, 0, len(numbs) - 1)


# random_list_of_nums = [22, 5, 1, 18, 99]
random_list_of_nums = list(range(100))[::-1]
print(random_list_of_nums)

quickSort(random_list_of_nums)
print(random_list_of_nums)
