#Using recursion find ways to get number of ways that matrix can be approached

# def grid_traveller(m,n):
#     if m== 1 and n==1:
#         return 1
#     if m==0 or n==0:
#         return 0
#     return grid_traveller(m-1,n)+grid_traveller(m,n-1)
# print(grid_traveller(2,3))

#memoization
# def grid_trav1(m,n, memo=None):
#     if memo is None:
#         memo = {}
#     key = (m,n)
#     if key in memo:
#         return memo[key]
#     if m==1 and n==1:
#         return 1
#     if m==0 or n==0:
#         return 0
#     memo[key] = grid_trav1(m-1,n,memo)+grid_trav1(m,n-1,memo)
#     print(grid_trav1(3,3))


#Tabulation method(bottom up)
# def grid_trav2(m,n):
#     table =[[0]* (n+1) for _ in range(m+2)]
#     table[1][1]=1
#     for i in range(m+1):


#WAP to read and print matrix element by end users
# matrix = []
# def matrix_of(i,j):
#     for i,j in matrix:
#         element = int(input(f"Element[{i+1},{j+1}]:"   ))
#         row.append(element)
#     matrix.append(row)
#     print("/nThe matrix is:")
#     for row in matrix:
#         print(" ".join(map(str,row)))


# def matrix1(m,n):
#     matrix=[]
#     for i in range(m):
#         row=[]
#         for j in range(n):
#             p=int(input(f"Enter the values{i+1}{j+1}"))
#             row.append(p)
#         matrix.append(row)
#         for r in matrix:
#             print(r)
# print("Matrix Values")
# n = int(input("Enter the numbr of columns:"))
# m = int(input("Enter the numbr of rows:"))
# matrix1(3,4)

#Tabulation method
# def grid_traveller2(m,n):
#     table = [[0] * (n+1) for _ in range(m + 1)]
#     table[1][1] = 1
#     for i in range(m+1):
#         for j in range(n+1):
#             current = table[i][j]
#             if j+1 <=n:
#                 table[i][j + 1] +=current
#             if i+1<=m:
#                 table[i +1][j] +=current
#     return table[m][n]
# print(grid_traveller2(2,3))

#WAP to find fibanocci series nth value with the help of tabulation method

#pseudo code
# arr=[0,1,0]
# a[1]=1
# for i  in range(2,1):
#     a[i] = (i-1)+(i-2)
# n=3

 #code








#1) File handling
# file = open("Reverse_array_assignment1.txt")
# print(file.read())

 #OR
# 2) with open('Reverse_array_assignment1.txt') as f:
#     print(f.read())

# 3) Read single line from readline()
# file= open("Reverse_array_assignment1.txt","r")
# print(file.readline())

# 4)Read a single character
# with open("Reverse_array_assignment1.txt") as f:
#     print(f.read(5))

# 5) Iterator method
# with open("Reverse_array_assignment1.txt") as f:
#     for i in f:
#         print(i)

# 6) Create a file
#file=open("FileHandling_1.txt",'x')

#7) Writing and creation
# file=open("FileHandling.txt","w")
# file.write("Hello!,How are you")

# 8) For deleting we have to use os module
# import os
# os.remove("FileHandling.txt")
# file=open("FileHandling.txt")
# print(file)

#Q1) WAP to create a file with a statement "hello!", next line"hi",
# 3r line" how are you" ,4th line "good afternoon".
#check how manny lines started with h and how manny lines ended
#  with g remove the file from os

# file=open("FileHandling.txt","w")
# file.write("hello! \nhi \nhow are you \ngood afternoon")
# file.readline()
# count=0
# if(file[0] =="h"):
#     count+=1
# file.readline()
# if(file[0] =="h"):
#     count+=1
# file.readline()
# if(file[0] =="h"):
#     count+=1
# file.readline()
# if(file[0] =="h"):
#     count+=1
# print(count)


# 9) Exception Handling
# try:             #line cousing error is kept under try block
#     print(x)
#     print("hello")
# except:
#     print("handle")
# else:            #when try block is not cousing an error then else exexutes
#     print("else block")
# finally:
#     print("finally statement")

#PROJECT
#10) Display current time from os and clear the screen after 
# display

#import datetime
# from datetime import datetime
# current = datetime.now()
# print(current)
# time_string = current.strftime("%H :%M :%S")
# print(time_string)

#WAP to display formatted time with the help of strftime as 
#a method
# import datetime
# current = datetime.datetime.now()
# time_string = current.strftime("%H :%M :%S")
# print(time_string)
# date_str=current.strftime("%d %B %Y")#d-date,B-fullyear name
# print(date_str)

import time
import datetime
import os
try:
    while True:
        now= datetime.datetime.now()
        time_string= now.strftime("%H :%M :%S")
        date_string= now.strftime("%d %B %y")

        os.system('cls' if os.name=='nt' else 'clear') #clear screen and update terminal
        print("Digital Clock")
        print("Time:",time_string)
        print("Date:",date_string)
        time.sleep(1) #To update for every one sec
except KeyboardInterrupt:
    print("\nClock Stopped")
