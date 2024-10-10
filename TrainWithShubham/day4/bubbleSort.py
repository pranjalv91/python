'''
Bubble Sort
'''

#list_for_sorting = [4,5,2]

list_for_sorting = [1,1,2,3,-1,4,-2,0,56,89,5]

for i in range(len(list_for_sorting)):
    for j in range(len(list_for_sorting)):
        if (list_for_sorting[i] < list_for_sorting[j]):
            temp = list_for_sorting[i]
            list_for_sorting[i] = list_for_sorting[j]
            list_for_sorting[j] = temp

print(list_for_sorting)