#Inheritence



#Instance



#WAP to demoonstrate class methods and 
# static methods , instance method present in student class where static method contains printing of hello statement
#and remaining 2 methods are giving greetings to the end user like good morning

# class Student:
#     name="" 
#     email =""
    
#     def __init__(self, name,email):
#         self.name=name
#         self.email=email
    
#     @staticmethod
#     def display():
#          print("hello")

#     # @classmethod
#     # def display(cls):
#     #      print("hello world")
# s1 = Student
# Student.display()
# # Student.display()


#Creating object of superclass and sub class 
# class Parent:
#     def display(self):
#         print("My  property Parent Class")
# class Child(Parent):
#     def dispaly1(self):
#         print("This is Child class Property")

# p=Child()
# p.display()
# p.dispaly1()


#WAP to demonstrate single or simple inheritance with the help of real world senerio of chatgpt,
#  where parent class is gpt3.5 and the sub class is gpt4. In both the classes write one one method
#  to display statement like "from which class the property is taken".
# class gpt3_5:
#     def display(self):
#         print("from gpt3_5 the property is taken")
# class gpt4(gpt3_5):
#     def dispaly1(self):
#         print("from gpt3_5 the property is taken")

# p=gpt4()
# p.display()
# p.dispaly1()

# class Whatsappv1:
#     def whatsappv1(self):
#         print("This version only contains Text message")
# class Whatsappv2(Whatsappv1):
#     def whatsappv2(self):
#         print("This version contains vedio and audio")
# class Whatsappv3(Whatsappv2):
#     def __init__(self):
#         super().__init__()
#     def whatsappv3(self):
#         print("This version contains payment module")

# v3=Whatsappv3()
# v3.whatsappv1()
# v3.whatsappv2()
# v3.whatsappv3()

#when more then 1 class as super type and child class is 1 is multiple inheritance
#multiple inheritence

# class Car:
#     def printCarDetails(self):
#         print("Car details")
# class Bus:
#     def printBusDetail(self):
#         print("Bus details")


#Dynamic Programming

# memo = {}
# def stepPerm(n):
#     if n < 0:
#         return 0
#     elif n <=1:
#         return 1
#     if n in memo:
#         return memo[n]
#     memo[n] = (stepPerm(n-1)+stepPerm(n-2)+stepPerm(n-3))
#     return memo[n]


#WAP to design the nth fibonacci number with the help of dynamic programming
# def fibonacci(n):
#     if n <= 1:
#         return n
#     fib = [0] * (n + 1)
#     fib[1] = 1

#     for i in range(2, n + 1):
#         fib[i] = fib[i - 1] + fib[i - 2]

#     return fib[n]


#madam solution
# n = int(input("Enter the value of n: "))
# print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

# def fibonacci(n,memo={}):
#     if n in memo:
#         return memo[n]
#     if n<=1:
#         return n
#     memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
#     return memo[n]
# print(fibonacci(15))

#Q1-WAP to display factorial of n 
#goal: calculate factorial of n using recursion+ memoization


# def factorial(n,memo={}):
#     if n in memo:
#         return memo[n]
#     if n<=1:
#         return 1
#     memo[n]=n*factorial(n-1)
#     return memo[n]
# print(factorial(5))

#Q2-Climbing stair problem
#goal:count the ways to reach the top of stairs by taking 1 of 2 steps

#Grid problems
#Q1- Coin change problem
#goal: Find the minimum number of coins needed to make a given amount.
#Memoization used-stores results for smaller amount to avoid repeted calculations
# def coin_change(coins, amount):
#     memo = {}

#     def dp(n):
#         if n == 0:
#             return 0
#         if n < 0:
#             return float('inf')
#         if n in memo:
#             return memo[n]
#         min_coins = float('inf')
#         for coin in coins:
#             res = dp(n - coin)
#             if res != float('inf'):
#                 min_coins = min(min_coins, res + 1)

#         memo[n] = min_coins
#         return memo[n]

#     result = dp(amount)
#     return result if result != float('inf') else -1
# coins = [1, 2, 5]
# amount = 11
# print(coin_change(coins, amount))

#Q2- Longest common Subsequence
#goal:Find the length of the longest Subsequence common to 2 space
#Memoization use- Reduces overlapping subproblems in recursion

def long_com_sub(s1,s2):
    memo={}
    def dp(i,j):
        if i==len(s1) or j==len(s2):
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        if s1[i]==s2[j]:
            memo[(i,j)]=1+ dp(i+1,j+1)
        else:
            memo[(i,j)]= max(dp(i+1,j),dp(i,j+1))

        return memo[(i,j)]
    
    return dp(0,0)

s1 = "abcde"
s2 = "ace"
print(long_com_sub(s1, s2))

#Q3)Grid traveller problem
#goal:Count ways to travel from top left to bottom right in a grid moving
#only right to down
#Memoization use - Catches path to avoid recomputation


def grid_traveller(s1,s2):
    memo={}
    def dp(i,j):
        if i==0 or j==0:
            return 0
        if i==1 or j==1:
            return 1
        if (i,j) in memo:
            return memo[(i,j)]
        
        memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
        return memo[(i, j)]

    return dp(s1, s2)



#Q4) Edit distance
#goal: Find minimum operations to convert one string to another
#Memoization use - Stores intermediate transformations steps







