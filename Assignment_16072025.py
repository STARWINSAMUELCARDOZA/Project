#Q1)Write a function that takes a list of email addresses and returns only the valid ones.
#An email is considered valid if:
#It contains exactly one @ symbol.
#The domain part (after @) ends with .com or .in.
#The username part contains only alphanumeric characters and no spaces.

# def get_valid_emails(email_list):
#     valid_emails = []
#     for email in email_list:
#         # Check if there is exactly one '@'
#         if email.count('@') != 1:
#             continue
        
#         username, domain = email.split('@')
#         if not (domain.endswith('.com') or domain.endswith('.in')):
#             continue
#         if not username.isalnum():
#             continue
        
#         valid_emails.append(email)
    
#     return valid_emails

# emails = [
#     "john123@example.com",
#     "jane.doe@website.in",
#     "hello@world.org",
#     "invalid@@example.com",
#     "noatsymbol.com",
#     "user@site.com",
#     "user name@site.com",
#     "user@site.in"
# ]

# print(get_valid_emails(emails))


#Q2)Given a paragraph, write a function to return the top 3 most frequent words, ignoring case and punctuation.
#Use lower(), replace() to remove punctuation, and split() to break words.
#Use a dictionary to count frequencies, and sort by value.

# def top_3_words(paragraph):
#     paragraph = paragraph.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    
#     words = paragraph.split()  
#     freq = {}  

#     for word in words:
#         freq[word] = freq.get(word, 0) + 1  # Increment count
#     sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)

#     # Return top 3 words only
#     return [word for word, count in sorted_words[:3]]
# text = "Hello, hello! How are you? Are you fine? Hello!"
# print(top_3_words(text))


#Q3)You’re given a string of comma-separated names like " john,DOE, alice ,BOB ".
# Write a function that:
# Strips extra spaces
# Capitalizes each name properly (e.g., "John", "Doe")
# Returns a sorted list of names.
# Use strip(), title(), split(), and sort().

# def clean_and_sort_names(name_string):
#     names = name_string.split(',')  # Split by comma
#     cleaned_names = [name.strip().title() for name in names]  # Strip spaces & capitalize
#     cleaned_names.sort()  # Sort alphabetically
#     return cleaned_names
# input_str = " john,DOE, alice ,BOB "
# print(clean_and_sort_names(input_str))


for i in range(4,-1,-1):
    print (str(i) *i)