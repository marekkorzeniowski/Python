
def ifOdd (number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def collatzSeq ():
    print("Enter your number: ")
    numb = int(input())
    while numb != 1:
        print(numb)
        numb = ifOdd(numb)
        if numb ==1:
            print(numb)

collatzSeq()

