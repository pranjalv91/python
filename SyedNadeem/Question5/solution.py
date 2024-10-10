# A = [7, 2, 3, 1, 5, 6]
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

second_smallest_element = list_to_sort[1]
print("Second smallest element in the list is:",second_smallest_element)