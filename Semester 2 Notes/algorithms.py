#algorithms.py

def linearSearch(list,target):
    #it finds the index of the target
    curr = 0
    for i in range(len(list)): #takes at least 1 execution and at most len(list) executions
        curr = i
        if list[i] == target:
            return i, curr
        
    return "not found"


def binarySearch(list,target,curr_iter):
    mid = len(list)//2
    #Base Case
    if list[mid] == target:
        return target, curr_iter
    
    #Recursive Case:
    if list[mid] < target:
        return binarySearch(list[mid:],target,curr_iter+1)
    
    if list[mid] > target:
        return binarySearch(list[:mid],target,curr_iter+1)
    
""" 
Linear vs Binary Search is that binary search was way faster on sorted data. The last we're covering this year is a topic
called algorithmic complexity (complexity theory). 

Really we can break down a computational problem into three parts
    1) The input size
    2) How long the execution takes <- measuring this is nontrivial 
    3) The output
    

Thought Question:
    - If I ran the same piece of code on two different computers (with different specs), will these two programs execute
    in the same amount of time? No, the faster computer (the more optimized for this task) will obviously finish first
    even if its the same piece of code
    
    - We can't use raw timestamps as a way to measure efficiency with our program <= this is too subjective based on 
        - computer specifications
        - Quantum Electrodynamics 
        
    - We need some objective measure to determine the efficiency of our programs.
"""
    
nums = [num for num in range(9999)]

print(linearSearch(nums,847))
print("--")
print(binarySearch(nums,847,0)) #binary is much faster 


""" 
What do you think is a good objective measure to test how long a program takes to execute? In linear search vs binary search

I used the amount of comparisons each algorithm took to find the target. More generally I could use: 
    - How many lines of code were executed in our program. We call 1 line of code being executed = 1 CU 
    
    CU = Computational Unit
    
    If we're the same piece of code on two computers, the amount of CUs is the same (because its the same program)
    
The idea is: We can compare the efficiency of two different algorithms by looking at how many CUs each algorithm uses. 

To formalize what we're looking at: Consider this scenario
    1) For a generic program we are ALWAYS inputting a data structure of size n
    2) We want to measure how the WORST case scenario for our algorithm (what is the most amount of CUs taken for the worst case)
    3) MAX CUs = O() <- whatever is the maximum amount of CUs
    
    
"""

def linearSearch(list,target):
    #it finds the index of the target
    curr = 0
    for i in range(len(list)): #takes at least 1 execution and at most len(list) executions
        curr = i
        if list[i] == target:
            return i, curr
        
    return "not found"

""" 
Let's create a list of [1,2,3,4,5] 

Best Case: 1 CU
WORST Case: 5 CUs, 

len(list) = n = 5 CUs

Linear Search = O(n) <- in terms of growth

n is the size of the list

CUs = n <- what is the shape of this graph? This is a line

Linear Search's worst case grows at a linear rate based on the input size

Linear Search's main computational tool is a for-loop that goes over the entire list

1-for-loop = O(n)

"""

def foo():
    count = 0
    for i in range(2):
        for j in range(2):
            print(i,j)
            count +=1
    print(count)
foo() 

""" 
2:4
5:25
10:100

x:x^2

1 for-loop (linear search) = has a worst Case of O(n)
2 for-loops = has a worst case of O(n^2)

between n and n^2, which one grows faster? n^2. So a program running in O(n^2) is bad because it takes up n^2 CUs on the worst
case

For enterprise level programs, the inputs on these lists can be in the millions and billions

1000000**2


"""

def bar(list):
    print(1)
    
""" 
O(1), constant time. 

O(1)
O(n)
O(n^2)

Let's go back to binary search
"""

def binarySearch(list,target,curr_iter):
    mid = len(list)//2
    #Base Case
    if list[mid] == target:
        return target, curr_iter
    
    #Recursive Case:
    if list[mid] < target:
        return binarySearch(list[mid:],target,curr_iter+1)
    
    if list[mid] > target:
        return binarySearch(list[:mid],target,curr_iter+1)
    
"""
[1 ... 100]

target: 87 
input: entire list [1-100] len(list)
step 1: compare 50 to 87, throw away everything less than 50

target: 87
input: 1/2 of step 1 [50-100] len(list)/2
step 2: compare 75 to 87, throwing away everything less than 75

target: 87
input: 1/2 of step 2 [75-100] (len(list)/2)/2
step 3: comparing 87 to 87 So we're done

At every step we're halving the length of the search space. Do we know which mathematical function corresponds to DOUBLING  
the size of something at every x 

1,2,4,8,16,32 = 2^x = exponential growth

32,16,8,4,2,1 = log_2(x) in CS, every log is base 2, log(x). 

Binary search HALVES the search space at every step. What is it's big O computational complexity? O(log(n))


5. O(n^2)
4. O(n log n)
3. O(n)
2. O(log(n))
1. O(1)

Linear Search is O(n)
Binary Search is O(log n)

this is cycles 1-3 of Honors DSA

"""