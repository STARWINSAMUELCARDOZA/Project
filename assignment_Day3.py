#Q1)Write a function that takes a list of email addresses and returns only the valid ones.
#An email is considered valid if:
#It contains exactly one @ symbol.
#The domain part (after @) ends with .com or .in.
#The username part contains only alphanumeric characters and no spaces.

# def valid_emails(emails):
#     valid_mails=[]
#     for email in emails:
#         count=0
#         for i in email:
#             if i == '@':
#                 count+=1
#         if(count !=1):
#             continue

#         username, domain = emails.split('@')
#         if not (domain.endswith(".com") or domain.endswith(".in")):
#             continue
#         if not username.isalnum():
#             continue
#         valid_mails.append(email)
    
#     return valid_mails

#     mails=["amit@gmail.com","sam@nmamit.in","s nd@nmamit.in"]
#     print(valid_emails(emails))

#WAP to check wheater the givrn strings are examples of anagramm or not
var1 = 'abc'
var2 ='jcb'
s1=''.join(i.lower() for i in var1 if i.isalpha())
s2=''.join(i.lower() for i in var2 if i.isalpha())
if(sorted(var1)==sorted(var2)):
    print("Anagram")
else:
    print("Not anagram")