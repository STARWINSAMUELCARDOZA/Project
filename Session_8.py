
#phibolasis number
# WAP to find nth fibonacci series with a help of recursive
# 
# 
# def fibonacci(n):
#     if n<0:
#         return "not defined"
    
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
#     s=int(input("Enter a number: "))
#     print(fibonacci(s))

#WAP to display list of fibonacci number
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# def fibonacci_list(count):
#     fib_list = []
#     for i in range(count):
#         fib_list.append(fibonacci(i))
#     return fib_list

# # Example usage:
# num = int(input("Enter how many Fibonacci numbers to display: "))
# print("Fibonacci Series:", fibonacci_list(num))

#lambda
# cube = lambda x: x**3


# def fibonacci(n):
#     # return a list of fibonacci numbers
#     fib = [0,1]
#     for i in range(2,n):
#         fib.append(fib[i-1]+fib[i-2])
#     return fib[:n]    
    
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))


#WAP to display armstrong numbers in a given range# n=153
# def is_armstrong(num):
#     power = len(str(num))
#     sum_of_powers = sum(int(digit) ** power for digit in str(num))
#     return num == sum_of_powers

# start = 0
# end = 153

# print(f"Armstrong numbers between {start} and {end}:")
# for number in range(start, end + 1):
#     if is_armstrong(number):
#         print(number)

# write a tracing of four stairs having n values with 1,2,3, 
# display the number of permutations that we have to reach stair case

#important w.r.t interviews
# import os
# memo={}
# def stepPerms(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     elif(n<=2):
#         return n
#     if n in memo:
#         memo[n]
#     memo[n]=(stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3))%10000000007
#     return memo[n]

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#WAP to demonstrate set methods which shoould contain add, remove , discard, 
# pop ,length methods and display the values
#initial set:1,11,17,True,21,21,1,True
#add 7 to the set
#remove 1 from the set
#discard True

# collection = {1,11,17,True,21,21,1,True}
# print(collection)

# collection = set()
# print(type(collection))

# collection = set()
# collection.add(7)
# collection.pop(1)
# collection.discard(True)
# print(collection)


class solution:
    def intersection(self,nums1:List)








#memoisation
