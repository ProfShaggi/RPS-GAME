# List and tuples

#Create a list that contains 5 names
Names= ['Fred', 'Segun', 'Sam', 'Ola', 'Kelvin']
print(Names)
# Add two more names (Martins and Bone)
Names.append('Martins')   #Note that (append) can only take one argument
#Use (extend) to add multiple arguments to the list
Names.extend(['Bone', 'Femi', 'Joy'])
print(Names)

# To insert names at the beginning of the list, I used (insert)
Names.insert(0, 'James')
print(Names)

# To remove names from th list
Names.remove('Fred')
print(Names)

# To delete the entire names on the list
Names.clear()

message= input("Enter Username\n")
print("Welcome", message)

fisrt= ["Fem", 2, "Dave", 3, 4, "Grav"]
second= ("Fem", 2, "Dave", 3, 4, "Grav")
third= {"Fem", 2, "Dave", 3, 4, "Grav"}

print(type(fisrt))
print(type(second))
print(type(third))