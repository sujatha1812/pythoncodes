1. #multiplies argument x with argument y
add = lambda x, y : x + y
print(add(10, 20))
 
print("\nResult from a Function")
def add_func(x, y):
    return x + y

print(add_func(10, 20))


2. #fibonacci series using lambda

from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1]) 

print(fib(5))

3. #multiply each number in the given list

a_list = [1, 2, 3]

multiplied_list = [element * 2 for element in a_list]

print(multiplied_list)

4.#number divisible by 9 in a list of numbers

a_list = [27,34,45,9]

data = [element /9 for element in a_list]

print(data)

5. #count the even numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,2,24,3,45,6,7,8] 
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        
print("Number of even numbers :",count_even)
