#This is a simple caluculator, it is built to do simple arithmetric like addition, subtraction, multiplication and division

#This calculator can only execute one operation at a time



# Take inputs from user and store it

operation= input(
"""
Please what operation will you like to perform ? Type
1. For Addition
2. For Subtraction
3. For multiplication
4. For division

"""
)


num1= int(input("Please enter first number : "))
num2= int(input("Please enter second number : "))

# Define an addition function

def add(num1, num2):
    return num1 + num2


# Define a subtraction funtion
def subtract(num1, num2):
    return num1 - num2


# Define a multiplication function
def multiply(num1, num2):
    return num1 * num2


# Define a division function
def divide(num1, num2):
    return num1 / num2





# The blocks of code below are conditional statement which checks the operation choosen and subsequently executes the function


if operation == "1":
    print('{} + {}'.format(num1, num2))
    print(add(num1, num2))
elif operation == "2":
    print('{} - {}'.format(num1, num2))
    print(subtract(num1, num2))
elif operation == "3":
    print('{} x {}'.format(num1, num2))
    print(multiply(num1, num2))
elif operation == "4":
    print('{} / {}'.format(num1, num2))
    print(divide(num1, num2))
else:
    print("You have not typed a valid operation number. Restart to choose a valid operation number ")







