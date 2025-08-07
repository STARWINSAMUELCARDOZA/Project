#Q1) Longest substring without repeating characters
# def length_longest_substring(s):
#     seen = set()
#     left = 0
#     max_len = 0

#     for right in range(len(s)):
#         while s[right] in seen:
#             seen.remove(s[left])
#             left += 1
#         seen.add(s[right])
#         max_len=max(max_len, right-left+1)

#     return(max_len)
# input_str = "abcabcbb"
# print("Input:", input_str)
# print("Output:", length_longest_substring(input_str))


#Q2 username Validator
import re

def is_valid_username(username):
    if not (6 <= len(username) <= 20):
        return False
    if not username[0].islower():
        return False
    if not re.fullmatch(r'[a-z0-9_.]+',username):
        return False
    specials = {'__','..'}
    for pair in specials:
        if pair in username:
            return False
    if username[0] in '._' or username[-1] in "._":
        return False
    return True

Eg_usernames = ["sam.car","a_b.c_d"]
for u in Eg_usernames:
    print(f"{u}: {'Valid' if is_valid_username(u) else 'Invalid'}")

