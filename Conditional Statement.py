
#Conditional Statement
cash = 20
if cash < 10:
    print('Buy chocolate')
else:
    print('insufficient fund')

#Multiple Conditions with "Elif"
    
Money = 30
if Money == 1000:
    print("He is Rich")
elif Money == 800:
    print('Not Very Rich')
elif Money == 500:
    print('Average class')
elif Money <= 499:
    print('He is below poverty line')
else:
    print('Not valid')

#Combining Conditions
money = 30
if money == 100 or money == 80 or money == 60:
    print('Sufficient fund')
else:
    print('Insufficient fund')

#Loops
#For loop (Automatic repetition)
for x in range(0, 5):
    print('Oluwasegun')

names = ['Adam', 'Titi', 'Femi']
for x in names:
    print(f'Hello {x}')

#Conditional statement and formatted string
Name = 'Mikel'
if Name == Name:
    print(f'Hello {Name}')

#WHILE Loop
#var = 5
#while var < 10:
    #print("endless loop")

#Nested Loop
for x in range(1, 13):
    for y in range(1, 13):
        print(f'{x} X {y} = {x * y}')
#print('=============')

