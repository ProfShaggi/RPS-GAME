#Data Collection (Lists)
PrimeNumbers = [2, 3, 5, 7, 11]
print(type(PrimeNumbers))
print(PrimeNumbers[3])

#To add '13' and remove '5' to the list above
PrimeNumbers = [2, 3, 5, 7, 11]
PrimeNumbers.append(13)
PrimeNumbers.remove(5)
print(PrimeNumbers)

#To remove multiple numbers from a list, instead of using the remove function, use 'clear'
PrimeNumbers = [2, 3, 5, 5, 3, 7, 7, 11]
PrimeNumbers.remove(5)
PrimeNumbers.remove(5)
PrimeNumbers.clear()
print(PrimeNumbers)

#Tuples
tuple1 = (5, 10, 'Segun', 4.7)
print(tuple1)
print(type(tuple1))

print(tuple1[2])
print(tuple1.index('Segun'))

#Converting a tuple into a list
TupleToList = list(tuple1)
print(TupleToList)
print(type(TupleToList))

NamesandID = ['Samuel', 1001, 'James', 1002,'Titi', 1003, 'Dayo', 1004]
ListToTuple= tuple(NamesandID)
print(NamesandID)
print(type(ListToTuple))


print(NamesandID[2])

age= 8
result= str(age)
print(type(result))

# def calculate(x, y):
#     global expression
#     expression = str(x + y)
#     result= str(eval(expression))
#     print(result)
# calculate(2, 4)
import math
def calculator(x, y):
    expression = (x + y)
    return math.sqrt(expression)
check= calculator(12, 778)
print(check)