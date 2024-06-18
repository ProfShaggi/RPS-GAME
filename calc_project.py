#Calculator project
#Import Tkinter for GUI

from tkinter import *
win = Tk()
win.title('Calculator')
win.geometry('515x365')
win.resizable(0, 0)

#Function to click the buttons
def button_click(item):
    global expression
    expression= expression + str(item)
    input_text.set(expression)

#Function to clear input field
def clear_button():
    global expression
    expression= ""
    input_text.set(expression)

#Function for the equal button
def equal_button():
    global expression
    result= str(eval(expression))
    input_text.set(result)
    expression= ""

#Using the StringVar to holds string variables inputed in the input field
expression = ""
input_text = StringVar()

#Creating the input field of the calculator in a frame
input_frame= Frame(win, width=312, height=50)
input_frame.pack(side=TOP)

#create an entry for the input frame
input_field= Entry(input_frame, font=('arial', 18, 'bold'), width=45, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

#Increase the height of input_field (Inner padding)
input_field.pack(ipady=10)

#Button Frame
button_frame= Frame(win, width=310, height=270)
button_frame.pack()

clear= Button(button_frame, text='C', width=38, height=3, command= lambda:clear_button()).grid(row=0, column=0, columnspan=3, padx=0.5, pady=0.5)
divide= Button(button_frame, text='/', width=10, height=3, command=lambda: button_click('/')).grid(row=0, column=3, padx=1, pady=1)

#Button Second Row
seven= Button(button_frame, text='7', width=10, height=3, command=lambda: button_click(7)).grid(row=1, column=0, padx=0.5, pady=0.5)
eight= Button(button_frame, text='8', width=10, height=3, command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine= Button(button_frame, text='9', width=10, height=3, command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply= Button(button_frame, text='*', width=10, height=3, command=lambda: button_click('*')).grid(row=1, column=3, padx=1, pady=1)

#Button Third Row
four= Button(button_frame, text='4', width=10, height=3, command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five= Button(button_frame, text='5', width=10, height=3, command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six= Button(button_frame, text='6', width=10, height=3, command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
plus= Button(button_frame, text='+', width=10, height=3, command=lambda: button_click('+')).grid(row=2, column=3, padx=1, pady=1)

#Button Fourth Row
one= Button(button_frame, text='1', width=10, height=3, command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two= Button(button_frame, text='2', width=10, height=3, command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three= Button(button_frame, text='3', width=10, height=3, command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
minus= Button(button_frame, text='-', width=10, height=3, command=lambda: button_click('-')).grid(row=3, column=3, padx=1, pady=1)

#Button Fifth Row
zero= Button(button_frame, text='0', width=24, height=3,command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point= Button(button_frame, text='.', width=10, height=3,command=lambda: button_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal= Button(button_frame, text='=', width=10, height=3, command=lambda: equal_button()).grid(row=4, column=3, padx=1, pady=1)


win.mainloop()