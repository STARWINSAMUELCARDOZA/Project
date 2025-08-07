# def is_pallindrome_recursive(s):
#     s=s.lower()
#     def helper(left,right):
#         if left >= right:
#             return True
#         if s[left]!=s[right]:
#             return False
#         return helper(left+1,right-1)
#     return helper(0,len(s)-1)

# print(is_pallindrome_recursive("Madam"))
# print(is_pallindrome_recursive("racecar"))

def is_pallindrome_recursive(s,start=0,end=None):
    s=s.lower()
    end=len(s)-1

    if start>=end:
        return True
    if s[start] != s[end]:
        return False
    
        return is_pallindrome_recursive(s,start=1,end=1)
    
s=input("Enter a string")
print(is_pallindrome_recursive(s))
