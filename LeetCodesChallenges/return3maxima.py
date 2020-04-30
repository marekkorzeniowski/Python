listOfIntegers = [1, 2, 100, -2, 3, 4, 7, 8, 9, 0, 53, 76, 1000, 98]


def twoMaximaOfList (list):
    max = list[0]
    secMax = list[0]
    thirdMax = list[0]

    for int in list:
        if int > max:
            thirdMax = secMax
            secMax = max
            max = int
        elif int > secMax:
            thirdMax = secMax
            secMax = int
        elif int > thirdMax:
            thirdMax = int

    print(str(max))
    print(str(secMax))
    print(str(thirdMax))

twoMaximaOfList(listOfIntegers)


