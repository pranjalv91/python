import time

#Print first 10 even numbers using for loop
print("Print first 10 even numbers using for loop")
for i in range(0,20,2):
    print(i)

#Print first five intergers using while loop
print("Print first five intergers using while loop")
i = 0
while i < 5:
    print(i)
    i+=1

#Print hello every 2 seconds
#For this import time library
while True:
    time.sleep(2)
    print("Hello")
#Press Ctrl+C to stop the execution