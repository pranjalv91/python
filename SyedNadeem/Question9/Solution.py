input_string = input("Enter string to be checked for pallindrome: ")
string_to_check = ""

str_len = len(input_string)

i = 0
while i < str_len:
    string_to_check = string_to_check + (input_string[str_len - 1])
    str_len = str_len - 1

if (string_to_check == input_string):
    print("Input string is pallindrome")
else:
    print("Input string is not pallindrome")