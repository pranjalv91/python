#Define a list of envs
list_of_envs = ["dev","stg","prd"]

#Define key to be searched in the envs
key = "stged"

#Use a for loop to iterate over list of envs
for env in list_of_envs:

    #If the element matches the key print the message match found with the index in the list where key was found
    if env == key:
        print("Match found at index:",list_of_envs.index(key))
else:
    print("Match not found")
