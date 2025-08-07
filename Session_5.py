#Q1) Pattern
# c = 'H'
# n = 5
# for i in range(n-1):
#     print((c*i).rjust(n-1)+c+(c*i).ljust(n-1))
# for i in range(n):
#     print((c*n).center(5*2)+(c*n).center(5*6))
# for i in range(n):
#     print((c*n*n).center(5*6))
# for i in range(n):
#     print((c*n).center(5*2)+(c*n).center(5*6))
# for i in range(n):
#     print(((c*(n-i-1)).rjust(n)+c+(c*(n-i -1)).ljust(n)).rjust(n*6))


#Q2)Find a string
# s="ABCCDCDC"
# s1 = "CDC"
# count = 0
# s2=[]
# for i in range(len(s)):
#     if s[i:i+len(s1)]== s1:
#         count+=1
#         s2.append(s1)
# print(count,s2)

#WAP to check wheather given number is amstrong number or not

# n=153
# d = 0
# m=n
# num = n
# while num>0:
#     count+=1
#     rem =n%10
#     d +=1
#     num=num//10
#     sum=0
    
#     print(n)
#     print(d)

#Q5)Average Calculator

# names = ['bac','abc','xyz','mno']
# n1 =[24,22,50,23]
# n2 = [50,43,33,45]
# str1='xyz'
# for i in range(len(names)):
#     if names[i]==str1:
#         index = i
#         break
# print((n1[i]+n2[i])/2)

#Q6) Valid signup details:
#WAP to compare adjacent element in the list. if 2 adjusent elements are
# same move that element to resultant list and print unique element list
# which is containing all uniquely entered value present in the input list

# names = ['a@gmal.com', 'b2gmail.com','a@gmail.com']
# uniquelist = []
# for i in range(len(names)):
#     if names[i] not in uniquelist:
#         uniquelist.append(names[i])
# print(uniquelist)
    
#write a program to find targetted element in a list
# def findindex(inputlist,target):
#     for index in range(len(inputlist)):
#         if inputlist[index]==target:
#             return index
#     return -1

# print(findindex(['a@gmail.com','b@gmail.com','a@gmail.com','c@gmail.com','g@gmail.com'],'z@gmail.com'))


#number guessing game 
# import random
# secret_no = random.randint(1,10)
# while True:
#     entered_no =int(input("Enter your number: "))
#     if secret_no - entered_no ==0:
#         print("Congrates")
#         break
#     elif secret_no - entered_no >2:
#         print("Hot")
#         print('\U0001F564')
#     elif secret_no - entered_no <=2:
#         print("cold")
#         print('\U0001F528')
        
#WAP to display count of given number in a list
# lst = [7,49,7,6,41,7,1,101]
# targeted_no = 7
# count =0
# for i in range(len(lst)):
#     if lst[i] == targeted_no:
#         count+=1
# if count==0:
#     print("not found")
# else:
#     print(count)

#WAP to check pallindrome
s= "abadc"
if s==s[::-1]:
    print(True)
else:
    print(False)    

#WAP using function that calculates and returns the total price of a item including Tax
#senerio: This prog. works for small shop where the user enters the prize of a item and
#  we have list of Tax amount
# Tax_List = [3,5,7]
# List_of_items = ["books", "pen", "mobile"]

# tax_mapping = dict(zip(List_of_items,Tax_List))
# def calculate_total_price(item_name, item_price):
#     if item_name.lower() in tax_mapping:
#         tax_rate = tax_mapping[item_name.lower()]
#         total_price = item_price + (item_price * tax_rate)
#         return total_price
#     else:
#         print("Item not found in the list.")
#         return None

# # Example usage
# item = input("Enter the item name (books/pen/mobile): ").strip().lower()
# price = float(input("Enter the price of the item: "))

# total = calculate_total_price(item, price)
# if total is not None:
#     print(f"Total price for '{item}' including tax is: ₹{total:.2f}")

# l1 = ['books','pen','phone']
# l2 = [3,5,7]
# combined =list(zip(l1,l2))
# print(combined)
# for i,j in zip(l1,l2):
#     print(i,j)


def minion_game(string):
    vowels = 'AEIOU'
    k,s = 0,0
    l =len(string)
    for i in range(l):
        if string[i] in vowels:
            k += (l-i)
        else:
            s += (l-i)
    if k > s:
        print("Kevin", k)
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)