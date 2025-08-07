# s = 'ABCDEFGH'
# res = ''
# max=4
# for i in range(0,len(s),max):
#     res=res+(s[i:i+max] + '\n')
# print(res)


#WAP to print the given string is pallindrome or not
def palindrome(var):
    var=var.lower()
    l=[]
    for i in var:
        if i.isalpha():
            l.append(i)
    var1=''.join(l)
    rev=var1[::-1]
    for i in range(len(var1)):
        if(var1[i]!=rev[i]):
            return "Not Pallindrame"
    return "Pallindrome"

var1 = input("Enter the string: ")
print(palindrome(var1))

