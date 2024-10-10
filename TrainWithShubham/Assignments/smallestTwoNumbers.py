#Create an empty list
list_to_be_sorted = list()

#Enter the range for the list
total=int(input("Enter total number of elements to be added to the list:"))

#Create a for loop to input elements for the list
for i in range(total):
    num = int(input("Enter number to be added to the list:"))
    list_to_be_sorted.append(num)

#Use bubble sort to sort the list
for i in range(len(list_to_be_sorted)):
    for j in range(len(list_to_be_sorted)):
        if (list_to_be_sorted[i] < list_to_be_sorted[j]):
            temp = list_to_be_sorted[i]
            list_to_be_sorted[i] = list_to_be_sorted[j]
            list_to_be_sorted[j] = temp

#Print the sorted list
print(list_to_be_sorted)

#Print the smallest and second smallest number
print("Smallest number is: ",list_to_be_sorted[0])
print("Second smallest number is: ",list_to_be_sorted[1])