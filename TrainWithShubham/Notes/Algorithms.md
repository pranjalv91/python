# Algorithms

## Searching Algorithms
### Linear Search
list_of_envs = ["dev","stg","prd"]<br />
Value to search = "stg"<br />

**Step 1** = Start<br />
**Step 2** = Define the list of envs and the key to search<br />
**Step 3** = Use for loop to iterate through each element in the list<br />
**Step 4** = Use if condition to compare each element in list with key<br />
**Step 5** = if comparison is True = Element Found<br />
&emsp;&emsp;&emsp;&emsp;else Element not found<br />
**Step 6** = Stop<br />
<br />
**Time Complexity**<br />
for loop --> n times; O(n)<br />
if condition --> 1 time; O(1)<br />

## Sorting
### Bubble Sort Algorithms

**Step1** = Start<br />
**Step2** = Use a for loop to iterate over all elements of the list using variable i<br />
**Step3** = Use a second nested for loop to compare element i with all other elements in the list using variable j<br />
**Step4** = If the element at position i is less than element at position j, then swap the elements using a temporary variable<br />
&emsp;&emsp;**4a**) Place the value of the element at position i in the temp variable<br />
&emsp;&emsp;**4b**) Replace the value of element at position j with the value of element at position i<br />
&emsp;&emsp;**4c**) Finally use the value in the temp variable to replace the value of the element at position j<br />
**Step5** = Repeat this process for each of the remaining elements in the list to get the sorted list<br />
**Step6** = Stop<br />

**Time Complexity**<br />
Nested for loops<br />
for(n)<br />
&emsp;&emsp;for(n)<br />
TC: O(n^2) and not O(2*n)<br />

## Assigments
### Assigment 1
Input a list of Numbers from user i.e take integer inputs and append to list<br />
Find the smallest and Second Smallest Numbers from that list<br />

**Step1** = Start<br />
**Step2** = Create an empty list using [] brackets or using list() function<br />
**Step3** = Take user input for range ie. total number of elements to be added to the list. Cast the input from string to integer<br />
**Step4** = Use a for loop to iterate over the range to enter individual elements in the list. Cast each input from string to integer<br />
**Step5** = Use a for loop to iterate over the elements of the list<br />
**Step6** = Use another for loop to compare each element with every other element in the list<br />
**Step7** = If the element at position i is less than element at position j, then swap the elements using a temporary variable<br />
&emsp;&emsp;&emsp;**7a**) Place the value of the element at position i in the temp variable<br />
&emsp;&emsp;&emsp;**7b**)	Replace the value of element at position j with the value of element at position i<br />
&emsp;&emsp;&emsp;**7c**)	Finally use the value in the temp variable to replace the value of the element at position j<br />
**Step8** = Repeat this process for each of the remaining elements in the list to get the sorted list
**Step9** = Print the first element of the list to get smallest number<br />
**Step10** = Print the second element of the list to get second smallest number<br />
**Step11** = Stop<br />
