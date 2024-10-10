#Define variables
list_of_envs = ["dev","stg","prd","qa","testing"]
key = "testing"
isFound = False


for env in list_of_envs:
    if env == key:
        index = list_of_envs.index(key)
        isFound = True
        break

if isFound:
    print("Match found at index:",index)
else:
    print("Match not found")