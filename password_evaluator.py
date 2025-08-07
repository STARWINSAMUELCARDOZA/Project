import string

def evaluate_password(password):
    password = password.replace(" ", "")
    
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

password = 'A123@a'
evaluate_password(password)