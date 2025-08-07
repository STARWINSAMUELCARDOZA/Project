
# def find_one(nums):
#     nums = [1,7,7]
#     for i in range(len(nums)):
#        count = 0
#        if nums[1] =  


# s1 = {1,2,3,4,4,2,1}
# s2 = {1,2,3}
# s3 = s1^s2
# print(s3)

# result = 0
# for nums in s1:
#     result=result^nums
# print(result)


#No idea
# n , m=map(int,input().split())
# arr = list(map(int,input().split()))
# A=set(map(int,input().split()))
# B=set(map(int,input().split()))
# happiness=0
# for x in arr:
#     if x in A:
#         happiness+=1
#     elif x in B:
#         happiness-=1
# print(happiness)

#terminal to be given 
# 2 6
# 1 2 3 4 5 6 
# 1 2 3
# 4 5 6
#output in terminal
# 0


# s1=set(map(int,input().split()))
# s2=set(map(int,input().split()))
# s3 = s1^s2
# print(s3)
# print(sorted=s1^s2)



# n= int(input())
# countries =set()

# for _ in range(n):
#     countries.add(input().strip())
# print(len(countries))


# 3
# USA
# INDIA
# USA
#output
#2


#OOPs
# class Employee:
#     def display():
#         print("hello")
# #object
# e1= Employee()#Employee is a constructor
# e2= Employee()#Employee is a constructor
# e1.display() 
# print(e1)
# print(e2)

#WAP to create student class and print object reference
# class Student:
#     name = 'Sam'
#     email = 'sam@gmail.com'
#     def display(abc):
#         print(abc.name) #retrive name from variable abc
#         print(abc.email)
# s1 =Student()
# s1.display()
# print(s1)

#Take two variables as first name and the last name and display the values 
# with the help of function
# class Student:
#     firstname = 'Sam'
#     lastname = 'Rodrix'
#     def display(self):
#         print(self.firstname) #retrive firstname from variable abc
#         print(self.lastname) 
# s1 =Student()
# s1.display()
# print(s1)

#Implement multi user environment using constructor and 
#display the output
# class Student:
#     def __init__(Self,lastname,firstname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def __str__(self):
#         return self.lastname+self.firstname
#     def display(self):
#         print(self.firstname) #retrive firstname from variable abc
#         print(self.lastname) 
# s1 =Student("abc","xyz")
# s1.display()
# print(s1)
#simulate pre-defined str method to return a string which is containing username lname,
#firstname and lastname


#A class where we are taking properties from a class is Superclass/Baseclass
# class Class1:
#     x=10
#     print("this is Class1")

#     class Class2(Class1):
#         pass
# c1=Class2()

    #WAP to manage users of libraray by creating userId, username,user contact as
    # data members where add user,search user,list of users are function members
    #based on end user details and requirements create user management system
    #Note: To store the data use a dictionary called as user

# class User:
#     user = {}
#     def __init__(self,userId, username,usercontact):
#         self.userId = userId
#         self.username = username
#         self.usercontact = usercontact
    
#     def adduser(self,userId, username,usercontact):

#         pass
#     def searchuser(self, username):

#         pass
#     def listofusers(self):

#         pass
#     def __main__(self):
#         print("Enter 1.adduser\n 2.searchusers\n 3.listofusers")
#         option=input()
#         if option == '1':
#             users = int(input())
#             username = input()
#             username = input
#             self.adduser(userId,username,usercontact):
