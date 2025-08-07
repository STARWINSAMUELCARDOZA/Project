#Q1) solve me first


#Q2) Write a function
"""
cal = int(input())
if(cal%4==0):
    if(cal%100 == 0):
        if(cal%400 == 0):
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Not leap")
else:
    print("Not leap")
"""

#List

# a =[1,2,3,"hello",5.5,True]
# print(a[0],a[3])
# print(type(a))
# l = len(a)
# a[0] = 20
# for i in range(l):
#     print(a[i])

#Q3 Hacker rank List

# N = int(input()) 
# a = []
# for _ in range(N):
#     val = input().strip().split()
#     cmd = val[0]

#     if cmd =="insert":
#         index = int(val[1])
#         value = int(val[2])
#         a.insert(index,value)
#     elif cmd == "print":
#         print(a)
#     elif cmd == "remove":
#         value = int(val[1])
#         a.remove(value)
#     elif cmd == "append":
#         value = int(val[1])
#         a.remove(value)
#     elif cmd == "sort":
#         a.sort()
#     elif cmd == "pop":
#         a.pop()
       
#array sum
# def sumofarray(arr):
#     sum=0
#     for i in arr:
#         sum+=i

#     return sum
# print(sumofarray([1,2,3,4]))

#Hacker rank
# def compareTriplets(a, b):
#     lst = [0,0]
#     for i in range(len(a)):
#         if (a[i] > b[i]):
#             lst[0] +=1
#         elif(a[i] < b[i]):
#             lst[1] +=1
#         else:
#             lst[1] +=1
#             lst[0] +=1
#     return lst
# print(compareTriplets([1,3,5],[2,3,4]))


# def minimaxsum(arr):
#     answer=[]
#     for i in range(len(arr)):
#         sum=0
#         for j in range(len(arr)):
#             for i==j:
#                 continue
                

"""m = int(input())
for i in range(1,m):
    print(i(10**i)-i//9)
"""
#WAP to print prime numbers present in a even array
#
arr=[1,7,17,19,24,36,11,2,39]
primes=[]
for i in arr:
    if i==0 or i==1:
        continue
    isprime=True
    for j in range(2,i):
        if i%j==0:
            if j!=i:
                isprime=False
                break
    if isprime==True:
        primes.append(i)
print(primes)


