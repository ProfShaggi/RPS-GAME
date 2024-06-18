# for loop

# Names= ("Dave", "Bone", "Vage", "James")
# # for x in Names:
# #     print("Welcome", x)

# # # Break
# # for x in Names:
# #     if x == "Vage":
# #         break
# #     print(x)

# # Continue
# for x in Names:
#     if x == "Vage":
#         continue
#     print(x)

# Nested loop

# usernames= ("Adex", "Kerb", "Grays", "Iky")
# actions= ("Plays", "Eats", "Sleeps", "Jog")

# for action in actions:
#     for name in usernames:
#         print(name, action + ".")


# import sys
# Details= True
# while Details:

#     password= input("\nEnter Your Password\n")
#     if password == "Segs":
#         username= input("\nEnter Your Username\n")
#         print("Welcome on Board", username)
#         sys.exit()
#     else:
#         print("Invalid Password")
#     Details= input("\nWanna Try Again?\nYes\nNo\n\n")
#     if Details == "Yes":
#         continue
#     else:
#         print("You couldn't login😞😞😞")
#         sys.exit()
    
# Create a login page that allows the user to enter username and password

import sys
# Details= True
# while Details:
#     username= input("\nEnter Username\n")
#     if username == username:
#         password= input("\n\nEnter Password\n")
#         if password== "Segs":
#             print("Welcome Onboard", username)
#             sys.exit()
#         else:
#             print("Incorrect Password")
#         Details= input("\nDo You Want to Try Again?\n\nYes\nNo\n")
#         if Details== "Yes":
#             continue
#         else:
#             print("Sorry You Couldn't Login...😞😞😞")

# def login_details():
#     username= input("\nEnter Your Username\n")
#     mod_username= str(username)
#     if mod_username == username:
#         password= input("\nEnter Your Password\n")
#         if password == "dev":
#             print("Welcome On Board", username)
#         else:
#             print("Oops!😞 Wrong Password")
#             retry= input("\nWould you like to retry?\nYes\nNo\n\n")
#             if retry == "Yes":
#                 return login_details()
#             else:
#                 print("Sorry, you're not able to login. Try next time")
#                 sys.exit("Bye! 👋👋👋")
# login_details()

# Design a simple errand robot as function that automatically detect singular and plural in terms of quantity
def robot(location, item, quantity):
    print("Open the door")
    if quantity > 1:
        print(f"I'm going to {location}\nTo get {quantity} {item + "s"}")
    else:
        print(f"I'm going to {location}\nTo get {quantity} {item}")
    print("Good Bye 👋👋👋")
robot("Germany", "Apple", 1)

    


    






   



    
