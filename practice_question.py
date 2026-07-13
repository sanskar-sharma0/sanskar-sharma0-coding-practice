# # x = 10 
# # y = 3.5 
# # z ="vans"
# # print(x+y)
# # print(z+"sharma")

# # a = 5
# # a = 10 
# # b = a 

# # print (b)
# name = "sanskar"
# age = 19 
# # print ("my name is ",name,"and i am ",age,"years old.")
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# result = a + b
# print("result is :",result)
# a = 10 
# b = 3
# print("addition:,", a+b)
# print("subtraction", a-b)
# print("multiplication:", a*b)
# print("division:", a/b)
# print("modulus:", a%b)
# print("power:", a**b)
# x = 4
# y =4.0
# z = "4"
# print(type(x))
# print(type(y))
# print(type(z))
# a = input("enter value of a :")
# b = input("enterr value of b :")
# temp = a
# a = b
# b = temp
# print("after swapping;a =", a ,"b =", b)
# Name = input("Enter your name ::")
# age = input("enter your age ::")
# print ("hello"+Name +",you are"+ age +"years old.")
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
# print("Sum is:", x + y)

# calculator
# a = int(input("enter the number :"))
# b = int(input("enter the number :"))
# print("add",a+b)
# print("subtract",a-b)
# print("multiply",a*b)
# print("divide",a/b)
# print("reminder",a%b)
# print("xyz",a//b)
# print("bouble sata ",a**b)
# import tkinter as tk

# def click(event):
#     global expression
#     expression += event.widget["text"]
#     result_var.set(expression)

# def clear():
#     global expression
#     expression = ""
#     result_var.set("")

# def evaluate():
#     global expression
#     try:
#         result = str(eval(expression))
#         result_var.set(result)
#         expression = result
#     except:
#         result_var.set("Error")
#         expression = ""

# # GUI window setup
# root = tk.Tk()
# root.title("GUI Calculator")
# root.geometry("300x400")
# root.resizable(0, 0)

# expression = ""
# result_var = tk.StringVar()

# # Entry widget
# entry = tk.Entry(root, textvar=result_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify='right')
# entry.pack(fill='both', ipadx=8)

# # Button layout
# button_frame = tk.Frame(root)
# button_frame.pack()

# buttons = [
#     ['7', '8', '9', '/'],
#     ['4', '5', '6', '*'],
#     ['1', '2', '3', '-'],
#     ['C', '0', '=', '+']
# ]

# for row in buttons:
#     row_frame = tk.Frame(button_frame)
#     row_frame.pack(expand=True, fill='both')
#     for btn_text in row:
#         btn = tk.Button(row_frame, text=btn_text, font="Arial 18", height=2, width=4)
#         btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)

#         if btn_text == "C":
#             btn.config(command=clear)
#         elif btn_text == "=":
#             btn.config(command=evaluate)
#         else:
#             btn.bind("<Button-1>", click)

# root.mainloop()
# n = 15
# m = 7
# ans1 = n+m

# print("add of",n,"and",m,"is",ans1)
# ans2 = n-m
# print("subtractof",n,"and",m,"is",ans2)
# ans3 = n*m
# print("multiply of",n,"and",m,"is",ans3)
# ans4 = n/m
# print("divide of",n,"and",m,"is",ans4)
# ans5 = n%m
# print("modulus of",n,"and",m,"is",ans5)
# ans6 = n//m
# print("floor division of",n,"and",m,"is",ans6)
# calculator
# a = int(input("enter the number :"))
# b = int(input("enter the number :"))
# print("add",a+b)
# print("subtract",a-b)
# print("multiply",a*b)
# print("divide",a/b)
# print("reminder",a%b)
# print("xyz",a//b)
# print("bouble sata ",a**b)


