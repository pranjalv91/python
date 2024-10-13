## Data Structures and Algorithms

### Primitive Data Types
- Can hold only single value of data
- Has the following types
	- Integer
	- Float
	- String
	- Boolean

### Non primitive Data Types
- Can hold multiple values of data in a single structure. Has 2 types
  
#### Linear
- Used to store data in a consecutive/sequential manner
	- List
	- Tuple
	- Set
	- Dictionary

#### Non Linear
- Used to store data in a non-consecutive/non-sequential manner
	- Linked List
	- Graph
	- Trees
	

## Interview Questions

#### 1. Difference between list and array
- Array is used to store consecutive elements of similar type
- For eg.) when the list consists only of strings
names = ["abc","def","xyz"]
- In such a case the list will be treated as an array
- But if the list consists of mixed elements such as numbers,strings,boolean then it is treated like a list and not an array
list = [1,2,4,"abc","def","xyz",True]


#### 2. Difference between tuple and list
- Tuples are immutable; meaning once the values are defined they cannot be changed
- List are mutable; meaning they can be changed even the values are defined


#### 3. Why tuples are immutable
- Because the values in tuples are stored in the RAM memory as hash. 
  Hashes are assigned a fixed memory value
  Because of this processing time taken to process a tuple is less vs a list
- Use tuple only when you have priortize execution time and when values are fixed

### Sets
- Both sets and dictionaries are defined by {}
- So an empty set is actaully an empty dictionary by default
- An empty set should something called None in it (null set)
- So set_of_num = {} #Empty dictionary<br />
&emsp;&ensp;set_of_num = {None} #Empty Set<br />
- Set will only unique values by filtering out repetitive elements
- Set will only print the unique values in an ascending order irrespective of the order in they appear in the set
