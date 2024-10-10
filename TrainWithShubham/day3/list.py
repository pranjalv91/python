#How to define an empty list
#Lists are defined by square brackets []
list_of_names = list()
list_of_envs = []

#Define a list of elements 
list_of_envs = ["dev","stg","prd"]

#Print the first element of the list
print(list_of_envs[0])

#Index out of range error since 20th element does not exist
#print(list_of_envs[20])

#Using for loop to iterate the list
for i in list_of_envs:
    print("Deploying to",i,"env")

#Append an element to list by using user input
#newElement=input("Enter new element: ")
#list_of_envs.append(newElement)
#print("Print list after adding new element:",newElement)
#print(list_of_envs)

#Append an element to list
list_of_envs.append("client")
print("Print list after adding new element")
print(list_of_envs)

#Find what methods can used within list
#print(dir(list_of_envs))

#Find more specific information about a particular methods in list
#Use __doc__ after listname.method
print(list_of_envs.append.__doc__)
print(list_of_envs.insert.__doc__)
print(list_of_envs.remove.__doc__)

#Insert element at specific position in list
list_of_envs.insert(1,"testing")
print("List after inserting element",list_of_envs)

#Remove element at specific position in list
list_of_envs.remove("testing")
print("List after remove element",list_of_envs)