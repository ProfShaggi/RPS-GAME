#Data types 
# Strings
# Literal assignment

Firstname= 'Kelvin'
# Surname= 'Bone'
# print(type(Firstname))

# # Concatenation
# fullname= Firstname + " " + Surname
# print(fullname)

# # Concatenate string data with integer
# sentence= 'I like gospel music since'
# year= 1999
# conc= f'I like gospel music since {year}'
# conc += 's'
# print(conc)

# Multiple lines and escaping special characters
# multiline= '''Hey!\nHow are you doing?\n\t\t\tHi\n\t\t\tI'm doing good'''
# print(multiline)

# # String Methods
# print(Firstname.lower())
# print(Firstname.upper())

# print(multiline.title())
# print(multiline.replace('Hey', 'Hello'))

# Build a MENU
character= 'menu'.upper()
print(character.center(20, '='))
print('Menu List'.ljust(20, '-'))
print(" ")
print('Coffee'.ljust(16, '.'), '$5'.rjust(2))
print('Milk'.ljust(16, '.'), '$10'.rjust(2))
print('Chocolate'.ljust(16, '.'), '$20'.rjust(2))
print('Chicken'.ljust(16, '.'), '$30'.rjust(2))
print('Doughnut'.ljust(16, '.'), '$5'.rjust(2))

# Import module (math)
import math

print(math.pi)
print(round(math.sqrt(16)))
print(math.sin(20))


    
