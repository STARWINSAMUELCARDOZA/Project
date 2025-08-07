#logic-1
#Q2

# you = int(input("you:"))
# date = int(input("date:"))

# if(you>=8 or date>=8):
#     if(you<=2 or date<=2):
#         print("No")
#     else:
#         print("Yes")
# else:
#     print("Maybe")

#or
# def date_fashion(you,date):
#     if you<=2 or date<=2:
#         return 0
#     elif you>=8 or date>=8:
#         return 2
#     else:
#         return 1
    
#WAP to print the sum of digits present in the given number 
#n = 1234 o/p:10
n = 1234
sum = 0
while n>0: #while is used as we don't know the ending digit
    sum+=n%10
    n = n//10
print(sum)