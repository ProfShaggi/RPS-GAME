# MyAge = 32
# MyAge = MyAge + 1
# print(MyAge)

# rectanglelenght = 10
# rectanglebreadth = 5
# rectanglearea = rectanglelenght * rectanglebreadth
# print(rectanglearea)

# print(type(20))

# #Strings
# Content = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t".'
# print (Content)

# print('pytho' + 'n' + ' programming')

# #Strings (Embedding values in strings)
# myAge = 20
# myName = 'My name is Oluwasegun,'
# myMessage = '%s I am %s years old.'

# print(myMessage % (myName, myAge))

# #Strings (using "f" string)
# myAge = 20 + 5
# myName = 'My name is Oluwasegun,'
# myMessage = f'{myName} I am {myAge} years old.'

# print(myMessage)

# txt = 'Welcome to Shaggi Store'
# print(txt.capitalize())
# print(txt.upper())
# print(txt.count('o'))

# message = '''He said, "Aren't can't shouldn't wouldn't."'''
# print (message)

# Name = 'Oluwasegun Adelaja'
# Age = 25
# Status = 'Student'
# message = '%s is %s years old and a %s'
# print(message % (Name, Age, Status))

# #Using 'f' string
# Name = 'Oluwasegun Adelaja'
# Age = 25
# Status = 'Student'
# message = f'{Name.upper()} is {Age} years old and a {Status} '
# print(message)

Sentence = '''I'm at work\t Hey!\nHow are you doing?'''
Sentence = '''I'm at work\t Hey!\nHow are you doing?'''
print(Sentence)

print("Chocolate".ljust(20, "."), "$5".rjust(2))
print("Chocolate...........$5")


from enum import Enum
class rps(Enum):
    shoe= 1
    bag= 2
    cap= 3

choice= input("Number\n")
check= int(choice)

if check < 1 or check > 3:
    print("Not Valid Number")
elif check == 1:
    print("You choose", str(rps(check)).replace("rps.", ""))
elif check == 2:
    print("You choose", str(rps(check)).replace("rps.", ""))
elif check == 3:
    print("You choose", str(rps(check)).replace("rps.", ""))





