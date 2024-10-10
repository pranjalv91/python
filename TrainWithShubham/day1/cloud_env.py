#Enter input
env=input("Enter the cloud platform:")

# Check whether env is AWS or not
if env=="aws" or env=="AWS":
	print("You are in AWS environment")
else:
	print("You are not in AWS environment")