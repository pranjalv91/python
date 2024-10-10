# Function to return data type string
def extract_data_type(var):
    # Get the type of the variable 'var'
    type_str = str(type(var))

    # Extract the substring within the single quotes
    start_quote = type_str.find("'")  # Find the first occurrence of '
    end_quote = type_str.rfind("'")   # Find the last occurrence of '
    data_type = type_str[start_quote + 1:end_quote]

    #Return the extracted substring for data type
    return data_type


# Data Types in Python

#Example of Integer
a=900

#Example of Float
b=900.5

#Example of Boolean
value=True

#Example of String
name="Pranjal"

#Print values of variables
print("Value of variable a is",a)
print("Value of variable b is",b)
print("Value of variable value is",value)
print("Value of variable name is",name)

#Print data type
print("Data type of variable a with value",a,"is",extract_data_type(a))
print("Data type of variable b with value",b,"is",extract_data_type(b))
print("Data type of variable value with value",value,"is",extract_data_type(value))
print("Data type of variable name with value",name,"is",extract_data_type(name))

#Take user input. By default user input will be a string
num=input("Enter a number: ")
print("Data type of variable num with value",num,"is",extract_data_type(num))

#To make sure entered input is in integer and not in string we need to cast the value
num=int(input("Enter a number: "))
print("Data type of variable num with value",num,"is",extract_data_type(num))