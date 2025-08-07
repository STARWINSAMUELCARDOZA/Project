#tuples
# tup = (1,)
# print(type(tup))
# print(tup)

# #packing and unpacking
#t2=1,2,3,1
# print(type(t2))
# print(len(t2))
# print(min(t2))
# print(max(t2))
# print(t2.count(1))
# print(t2[1])

# #convertion from tuple to list
# l1 = list(t2)
# print(type(l1))

# #convertion from list to tuple
# l1 = tuple(t2)
# print(type(l1))

#WAP to create, insert, delete and display tuple values where input = 1,4,6,9
#add element =10 add even 2 remove element=2 display tuple elements

# tup1 = (1,4,6,9)
# print(type(tup1))
# l1 = list(tup1)
# l1.append(10)
# l1.append(2)
# print(l1)
# l1.remove(2)
# print(l1)
# print(type(l1))
# l2 = tuple(l1)
# print(type(l2))
# print(l2)

#membership operation(print with for:)
#for i in t2:
#    print(i)


#hash
# if __name__ == '__main__':
#     n = int(raw_input())
#     integer_list = map(int, raw_input().split())
#     tup1 =tuple(integer_list)
#     print(hash(tup1))

#dictionary

# d={
#     'name': 'abc',
#     'age':'21'
# }
# print(d)

# for i,h in zip(d.keys(),d.values()):
#     print(i,h)


#WAP to diclare dictionary with 3 key and value pair and print a dictionary
# dict1 = {
#     'name': 'starwin',
#     'age': 21,
#     'cgpa': 7.5
# }
# print(type(dict1))
# print(dict1)
# dict1['name'] = 'Starwin Samuel'
# dict1['surname'] = 'Cardoza'
# print(dict1.keys())
# print(type(dict1.keys()))

# print(dict1['name'])

# print(dict1.pop('age'))
# print(dict1.popitem())
# print(dict1)
#Note
#duplicate(repitation) values are allowed and duplicate keys not allowed


#WAP to display menu of a resturant with a key and value pair where keys are items available
# in a resturant and values are prices of the respective items.Take the order from end user 
# and generate invoice and display it.
 

# menu = {
#     'Masala Dosa' : 60,
#     'chapatti' : 35,
#     'poori' : 40,
#     'coffee' :20,
#     'tea' : 10
# }
# # print("Price:Masala Dosa:",menu['Masala Dosa'])
# # print("      Coffee:",menu['coffee'])

# for item,price in menu.items():
#     print(f"{item}: {price}")
#     order = input()
#     total = 0
# while True:


#Assignment
#WAP to maintain phonebook with a name and phone number 
# declare four methods such as add new contact, remove existing contact,
# search the contat with help of contact name and display.









#Write a prog to check wheather user entered nuumber is circular prime or not
#use 2 def functions to reverse a 2 digit number
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def reverse_2digit(num):
#     return (num % 10) * 10 + (num // 10)

# num = int(input("Enter a 3-digit number: "))

# if 10 <= num <= 999:
#     rev = reverse_2digit(num)
#     if is_prime(num) and is_prime(rev):
#         print(f"{num} is a Circular Prime.")
#     else:
#         print(f"{num} is NOT a Circular Prime.")
# else:
#     print("Please enter a 4-digit number only.")

#reverse number
# def reverse_2digit(num):
#     return (num % 10) * 10 + (num // 10)

# num = int(input("Enter a 2-digit number: "))
# if 10 <= num <= 99:
#     rev = reverse_2digit(num)
#     print(rev)
# else:
#     print("enter 2-digit number")

#or
def reversed_number(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)-rem
        n=n//10
        return rev
        print(rev)
n=13
reversed_number(n)
print(reversed_number(n))
