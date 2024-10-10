#Sets are defiend by {} bracket
#This is an example of empty dictionary not a set
set_of_num = {}
print(type(set_of_num))

#This is an example of empty set
set_of_num = {None}
print(type(set_of_num))

#Defining sets
set1 = {1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,45,4,34,3,2}
set2 = {1,1,1,1,1,1,45,6,6,6,6,6,6,7,7,7,8,4,3,3}

#Set Operations
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))

# Print list values before filtering duplicates
envs = ["dev","stg","prod","test","qa","qa","dev"]
print("Env values before filtering duplicates:",envs)

# Print list values after filtering duplicates
envs = list(set(envs))
print("Env values after filtering duplicates:",envs)