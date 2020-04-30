array = [4, -2, -8, 5, -2, 7, 7, 2, -6, 5]


def maxSumOfsublist(array):
    subsum = 0
    bestScore = 0
    for i in array:
            subsum = max(subsum + i, 0)
            bestScore = max(bestScore, subsum)
    print(bestScore)
    return bestScore
# maxSumOfsublist(array)

" maxSumTuple return tuple with starting index of subarray, index of the last element in the subarray which create maximal subsum of the input array"

def maxSumTuple(array):
    subSum = 0
    bestScore = 0
    curInd = startInd = bestInd = 0
    for ind, i in enumerate(array):
        if subSum + i > 0:
            subSum += i
        else: #reset of the position
            (subSum, curInd) = (0, ind + 1)
        if subSum > bestScore:
            result = (startInd, bestInd, bestScore) = (curInd, ind + 1, subSum)

    return result

print(maxSumTuple(array))
