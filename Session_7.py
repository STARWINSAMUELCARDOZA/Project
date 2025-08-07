#define function
# def function_name(*parameters): #To handle n number of input wich we do not know we use *
#     print(parameters)

# function_name(1,3)

# def function_name(name='abc',age=0):
#     print(name)
#     print(age)

# function_name(age=1,name=3)

#method over loading
# def add1(a,b):
#     print(a+b)
# # def add1(a=0):
# #     print(a)
# add1(18,6)

#WAP to display maximum number among 3 given integers. use function to do calculation.
#  Note inputs are integers not list.

# def max_function(a,b,c):
#     # a = 10
#     # b = 20
#     # c = 25
#     if(a>b and a>c):
#         print(a)
#     elif(b>a and b>c):
#         print(b)
#     else:
#         print(c)
# max_function(2,5,2)

#WAP to check and return true if a user -given number is the power of 2,
#else return false
# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     return (n & (n - 1)) == 0
# num = int(input("Enter a number: "))
# if is_power_of_two(num):
#     print("True")
# else:
#     print("False")

#or
# def powcheck(n):
#     while(n>1):
#         if(n%2==0):
#             n-n//2
#         else:
#             return False
#         return True
# def main():
#     n = 17
#     print(powcheck(n))
# main()

#WAP to check given num is perfect square root or not

# def is_squaroot_or_not(n):
#     while(n >= 2):


#when there is nothing to write in an function
# def my_function():
#     pass
# my_function()

#re-cursion is a function calling itself
#base condition required to terminate
# def greet(n):
#     print(n)
#     greet(n-1)
# greet(2)

# WAP to print even numbers present in the range of 1-10 without
# using looping control statements(use re-cursion method to solve)
# def even_no(n):
#     if(n<=10):
#         if(n%2==0):
#             print(n)
#         even_no(n+1)
# even_no(1)


#WAP to display list of a numbers present in the range of 1-100 
# which are completely divisible by 3 and 5 without using loop

# def divi_by3_by5(n):
#     if(n<=100):
#         if(n%3==0 and n%5==0):
#             print(n)
#         divi_by3_by5(n+1)
# divi_by3_by5(1)

#Factoral of a number:
# def fact(n):
#     if(n<0):
#         return
#     if(n==1):
#         return 1
#     else:
#         return fact(n-1)*n
# print(fact(5))

#game
def toweroftunnel(n, a, b, c):
    if n==1:
        print(f"Move disk1 from {a} to {c}")
        return
    toweroftunnel(n-1,a,c,b)
    print(f"move disk {n} from {a} to {c}")

    toweroftunnel(n-1, b,a,c)

n=3
toweroftunnel(n,'A','B','C')


#Devid's staircase
#WAP to