#Input two numbers 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Input the operator
operator = input("Enter operator: ")

#If-else conditional cases for operator
if operator == "+":
    output = num1 + num2
    print("Addition of",num1,"and",num2,"is",output)
    print(num1,"+",num2,"=",output)

elif operator == "-":
    output = num1 - num2
    print("Subtraction of",num1,"and",num2,"is",output)
    print(num1,"-",num2,"=",output)

elif operator == "*":
    output = num1 * num2
    print("Multiplication of",num1,"and",num2,"is",output)
    print(num1,"*",num2,"=",output)

elif operator == "/":
    output = num1 / num2
    print("Quotient of",num1,"and",num2,"is",output)
    print(num1,"/",num2,"=",output)

elif operator == "%":
    output = num1 % num2
    print("Remainder of",num1,"and",num2,"is",output)
    print(num1,"%",num2,"=",output)

else:
    output=None


#Less than, greater than and equal to
if num1 < 3:
    print("Num1",num1,"is less than 3")
elif num1 == 3:
    print("Num1",num1,"is equal to 3")
else:
    print("Num1",num1,"is greater than 3")