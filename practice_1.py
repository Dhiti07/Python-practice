#create a calculator using python
num1 = int(input("enter the 1st no.: "))
num2 = int(input("enter the 2nd no.: "))
operation = str(input("choose from sub,mul,add,div: "))
if operation == "add":
    print("your output is: ",num1+num2)
elif operation == "sub":
    print("your output is: ",num1-num2)
elif operation == "mul":
    print("your output is: ",num1*num2)
elif operation == "div":
    print("your output is: ",num1//num2)
