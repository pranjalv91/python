# A = [1, 10, 2, 6, 5, 3]
list_to_sort = []
size = int(input("Enter how many numbers to enter in the list: "))
temp = 0

for i in range(size):
    num = int(input("Enter number to be added to the list: "))
    list_to_sort.append(num)


for i in range(len(list_to_sort)):
    for j in range(len((list_to_sort))):
        if((list_to_sort[i]) < (list_to_sort[j])):
            temp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[j]
            list_to_sort[j] = temp

largest_element = list_to_sort[size - 1]
print("Largest element in the list is:",largest_element)

second_largest_element = list_to_sort[size - 2]
print("Second Largest element in the list is:",second_largest_element)

product_of_largest_two_numbers = largest_element*second_largest_element
print("Product of largest two numbers in the list is:",product_of_largest_two_numbers)