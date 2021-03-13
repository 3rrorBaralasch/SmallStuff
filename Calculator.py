def helpFunc():   
    print ("""
    Welcome to my Program, here you can do Text Mathematical Calculations.
    ......................................................................
    (!) Help
    -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    Functions:
    For Division--------------[D]
    For Multiplication--------[M]
    For Addition--------------[A]
    For Subtraction-----------[S]
    For Help------------------[H]
    To exit programm----------[E]
    """)

def userInput():
    num1 = input("Input your first number: ")
    num2 = input("Input your second number: ")
    return num1,num2

def main():

    CalcType = input("Please choose which calculation do you want to use: ")

    if CalcType == "D":
        num1,num2 = userInput()
        sum = float(num1)/float(num2)
        print(sum)
    elif CalcType == "M":
        num1,num2 = userInput()
        sum = float(num1)*float(num2)
        print(sum)
    elif CalcType == "A":
        num1,num2 = userInput()
        sum = float(num1)+float(num2)
        print(sum)
    elif CalcType == "S":
        num1,num2 = userInput()
        sum = float(num1)-float(num2)
        print(sum)
    elif CalcType == "H":
        helpFunc()
    elif CalcType == "E":
        exit()
    else:
        print("\nPlease type correct function name ;)\n")
    main()

#Calling Functions
helpFunc()
main()
