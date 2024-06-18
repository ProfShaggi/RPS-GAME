#Functions (Procedures/Method)
def get_milk():
    print('Take the money')
    print('Open the door')
    print('Lock the door')
    print('Walk to the door')
    print('Buy milk')
    print('Return home with milk')

get_milk()

#Parameters and Arguments
#The input in a function is called "Argument"

def get_milk(amount):
    print('Take the money')
    print('Open the door')
    print('Lock the door')
    print('Walk to the door')
    print(f'Buy {amount} milk')
    print('Return home with milk')

get_milk(10)

#Adding multiple "argument" to a function
#When executing the function, Note that the argument most be supplied in the order of the parameters declared in the function!
def get_milk(amount, destination):
    print('Take the money')
    print('Open the door')
    print('Lock the door')
    print(f'Walk to the {destination}')
    print(f'Buy {amount} milk')
    print('Return home with milk')

get_milk(20, 'New York')

#Using the "return" function in a def function to return the result of the function
def calculator(x, y):
    answer = x * y
    return answer
result = calculator(3, 5)
print(result)

# #Import statement (Modules or packages)
# import life
# value = life.Age
# print(value)

# #You can also import from file using the "from" function
# from life import Age, Name
# print(Age)
# print(Name)

# #You can also import from file using Eliasing "as" function
# import life as me
# value = me.Age
# print(value)

# life.big_theory

# value = life.square_root(225)
# print(value)


 