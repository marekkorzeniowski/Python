# Basic examples of list comprehensions

# output_list = [output_exp for var in input_list if (var satisfies this condition)]

#1 Create an output list which contains only the even numbers which are present in the input list
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output1 = [i for i in input_list if i % 2 == 0]
print(output1)

#2 create an output list which contains squares of all the numbers from 1 to 9

output2 = [i**2 for i in input_list]
print(output2)

# DICTIONARY COMPREHENSION

#d1  Create an output dictionary which contains only the odd numbers
# that are present in the input list as keys and their cubes as values.

output3 = {var : var**3 for var in input_list if var % 2 == 1 }
print(output3)


state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

myDict = {key:value for (key, value) in zip(state, capital)}
print(myDict)

# SET COMPREHENSION

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = {var for var in input_list if var % 2 == 0}
print(output_set)

# GENERATOR COMPREHENSION

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end=' ')

for var in output_gen:
    print(var, end=' ')


# MATRIX TRANSPOSITION

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposeMatrix = [[row[i] for row in matrix] for i in range(4)]
print(transposeMatrix)

#************ OR BETTER SOLUTION - using unpackin of the argument (opposite action of the intial action)
list(zip(*matrix))
