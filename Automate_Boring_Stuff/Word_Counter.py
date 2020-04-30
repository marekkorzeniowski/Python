
someText = "ala ma ala  i kot ma kot i dom dom jest duzy kot kot kot "
panTaduesz =open('Pan_Tadeusz.txt')

text = panTaduesz.read()

dictionary = {}
listOfStrings = someText.split()

for elemnt in listOfStrings:
    if elemnt in dictionary.keys():
        dictionary[elemnt] += 1
    else:
        dictionary[elemnt] = 1

for k,v in dictionary.items():
    print(f"{k} : {v}")

print(len(dictionary))
