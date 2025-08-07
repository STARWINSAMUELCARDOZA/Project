
#string methods
str1 = "Hello World!"
# str2 = "Hello"
# print(str1 + str2) #concatination
# print(str1,str2*3) #repeating of a string
# print(str1.lower()) #convert to lower
# print(str1.title()) #caps for first letter of a word
# print(str1.swapcase()) #swaps the case style each letter by letter
# print(str1.capitalize())

# s1 = input("Enter the string: ")
# print("The given sentence is  :"+" "+s1)
# print("After Case changed the string  is:"+s1.swapcase())

# class Solution(object):
#     def letterCasePermutation(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         s1 = input()
#         for i in range(s1):
#             return(+s1[i])

# print(str1)
# print(str1.find('d'))
# print(str1.index('o'))
# print(str1.count('a'))
# print(str1.startswith('H'))
# print(str1.endswith('u'))


#To implement simple ATM application, print the following application
# i) deposit
# ii)withdrawal
# iii)balance check
# iv)pin change

# pin =1234
# def deposit():
#     def withdraw():
#         balance = 1000
#         print("enter your pin number")
#         entered_pin = int(input())
#         if(entered_pin == pin):
#             choose = int(input())
#             if(choose==1):
#                 print("Enter amount to be depossited")
#                 amount = float(input())
#                 if amount <=0:
#                     print("invalid amount")
#                 else:
#                     print("amount deposited successfully")
#                     print(f"Deposited Amount:{amount+balance}")
#             else:
#                 if(entered_pin == pin):
#                     print("Enter amount to be withdraw:")
#                     amount = float(input())
#                 if amount <=0:
#                     print("invalid amount")
#                 else:
#                     print("amount withdrawn successfully")
#                     print(f"Withdrawal Amount:{amount-balance}")
#         else:
#             print("invalid pin number")
#     withdraw()
# deposit()

# balance=0
# pin =1234
# def deposit():
#     print("enter your pin number")
#     entered_pin = int(input())
#     if(entered_pin == pin):
#         choose = int(input())
#         print("Enter amount to be depossited")
#         amountdeposited = float(input())
#         if amountdeposited <=0:
#             print("invalid amount")
#         else:
#             print("amount deposited successfully")
#             print(f"Deposited Amount:{amountdeposited}")
#     else:
#         print("invalid pin number")        
#     deposit()

# def withdraw():
#     print("enter your pin number")
#     entered_pin = int(input())
#     if(entered_pin == pin):
#         print("Enter amount to be depossited")
#         amountwithdrawn = float(input())
#         if amountwithdrawn <=0:
#             print("invalid amount")
#         else:
#             print("amount deposited successfully")
#             print(f"Withdraw Amount:{amountwithdrawn}")
#     else:
#         print("invalid pin number")        
#     withdraw()

# def check_balance():
#     print(balance)

# deposit()
# withdraw()
# check_balance()

import string

def evaluate_password(password):
    password = p.replace(" ", "")
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    has_alpha = any(char.isalpha() for char in password)

    missing_criteria = []

    if not has_upper:
        missing_criteria.append("uppercase letter")
    if not has_lower:
        missing_criteria.append("lowercase letter")
    if not has_digit:
        missing_criteria.append("number")
    if not has_symbol:
        missing_criteria.append("symbol")
    if not has_alpha:
        missing_criteria.append("alphabet")

    if not missing_criteria:
        print("Strong Password")
    else:
        print("Weak Password. Missing:", ", ".join(missing_criteria))

password = 'St@1'
evaluate_password(password)

