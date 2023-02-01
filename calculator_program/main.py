import os
from art import logo

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

print(logo)
def calculator():

    flag=True
    n1=float(input("What\'s the first number: "))
    operation={
            "+":add,
            "-":sub,
            "*":multiply,
            "/":divide
        }

    for key in operation:
        print(key)
    choice=input("What operation you want to perform:")
    while flag:

        n2=float(input("What\'s the next number:"))
        calculate_function=operation[choice]
        first_answer=calculate_function(n1,n2)
        print(f"{n1}{choice}{n2}={first_answer}")
        choice1=input(f"type 'y' to continue calculating {first_answer},or 'n' to start new calculation :")
        if choice1=='y':
            n1=first_answer
        else:
            flag=False
            os.system('cls')
            calculator()
calculator()
