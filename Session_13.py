#Algorithms-Step by step process of achieving the solution
#applications- forward and backward navigation, finding 
# shortest route


#Q1) WAP to find number 7 in a given string without using pre-defined
# methods

# n=[1,3,5,7,9,11]
# count=0
# for j in n:
#     count+=1
#     for i in range(0,count):
#         if n[i]==7:
#             print(i)
#         else:
#             print()
    

#Binary search
#Set two pointers: low=0, high = length of array -1

# n=[1,3,7,5,9,11]
# target=7
# count=0
# low=0 
# high=len(n)-1
# mid=(low + high)//2
# if(n[mid]==target):
#     print(mid)
# elif(n[mid]<target):
#     low=mid+1
#     if(low==target):
#         print(low)
#     else:
#         low+=1
# elif(n[mid]>target):
#     high=mid-1
#     if(high==target):
#         print(low)
#     else:
#         high-=1
# else:
#     print("Not found")
    



#Stack - Last in First out(LIFO)
#It is a linear data structure that follows the Last-In-First-Out(LIFO)
#Applications- In navigation, in Redo and undo
#Stack with list has a drawback of number of elements size
#Push,pop,Peek,isEmpty,Size in built func

# stack = []
# def pushoperation(e):
#     stack.append(e)
#     print(stack)
# #pop operation
# def popOperation():
#     stack.pop()
#     print(stack)
# #check peek value
# def peekvalue():
#     print(stack[-1])
# #check empty or not
# def checklength():
#     print(len(stack))

# pushoperation(4)
# pushoperation(3)
# pushoperation(2)
# popOperation
# peekvalue()


#browser using stack
# backstack = []
# forward_stack = []
# currentpage = None

# def visit(page):
#     global currentpage
#     if currentpage is not None:
#         backstack.append(currentpage)
#     currentpage = page
#     forward_stack.clear()  
#     print(f"Visited Page: {currentpage}")

# def go_back():
#     global currentpage
#     if not backstack:
#         print("No page in history")
#         return
#     forward_stack.append(currentpage)
#     currentpage = backstack.pop()
#     print(f"Back to: {currentpage}")

# def go_forward():
#     global currentpage
#     if not forward_stack:
#         print("No forward page available")
#         return
#     backstack.append(currentpage)
#     currentpage = forward_stack.pop()
#     print(f"Forward to: {currentpage}")

# visit("www.youtube.com")
# visit("www.instagram.com")
# go_back()
# go_forward()          



#Design python classes or functions that use two lists to manage the history
#of typed characters. When a character is typed,it's pushed onto the main "main 
# content" stack. "deleted content" 

#Redo and Undo operation in text editors

undo_stack = []
redo_stack = []
current_state = None

def perform_action(action):
    global current_state
    if current_state is not None:
        undo_stack.append(current_state)
    current_state = action
    redo_stack.clear()
    print(f"Performed: {current_state}")

def undo():
    global current_state
    if not undo_stack:
        print("Not to undo")
        return
    redo_stack.append(current_state)
    action_type = current_state.split()[0]
    current_state = undo_stack.pop()
    print(f"Undo: {action_type}")

def redo():
    global current_state
    if not redo_stack:
        print("Not to redo")
        return
    undo_stack.append(current_state)
    current_state = redo_stack.pop()
    action_type = current_state.split()[0]
    print(f"Redo: {action_type}")

perform_action("Type 'Hello'")
perform_action("Type 'World'")
undo()
redo()


#Assignment -stack
# 1. Function Call Management (Call Stack)
# Real-World Usage: This is fundamental to how all programming languages (including Python) 
# execute code. Every time a function is called, its execution context (parameters, local 
# variables, return address) is "pushed" onto a special memory area called the "Call Stack".
# When a function returns, its context is "popped" from the stack, and execution resumes 
# from where it left off in the calling function.
# This is why recursive functions work: each recursive call pushes a new frame onto the 
# stack until a base case is reached, then frames are popped off one by one.
 
# Question:
# Scenario: You are analyzing how a simple Python program executes functions.
# Task: Given the following Python code, trace the contents of the "call stack" for the 
# calculate_total function step-by-step, starting from the main_program call.
















# 2. Real-World Usage: Compilers, interpreters, and scientific calculators often use 
# stacks to process and evaluate arithmetic expressions. Converting an "infix"
# expression (like 2 + 3 * 4) to "postfix" (Reverse Polish Notation, RPN, like 2 3 4 * +)
# simplifies evaluation because operator precedence is inherently handled.
# To evaluate a postfix expression, you read tokens from left to right.
# If you see an operand (number), push it onto the stack. If you see an operator, 
# pop the required number of operands from the stack, perform the operation, and
# push the result back onto the stack.
 
# Question:
 
# Scenario: You need to build a simple calculator that can evaluate expressions written in postfix notation.
# Task: Write a Python function evaluate_postfix(expression_string) that takes a string 
# containing a postfix expression (numbers and operatorsseparated by spaces) and returns 
# the result. Assume the operators are +, -, *, /.
# Example:
# evaluate_postfix("2 3 +") should return 5
# evaluate_postfix("2 3 4 * +") should return 14 (2 + (3 * 4))
# evaluate_postfix("10 5 / 2 +") should return 4.0 ((10 / 5) + 2)
# Hint: Use a list as your stack. When you encounter an operator, pop two operands, 
# perform the operation, and push the result.

# stack = []

# def evaluate_postfix(expression_string):
#     tokens = expression_string.split()

#     for token in tokens:
#         if token.isdigit(): 
#             stack.append(int(token))
#         elif '.' in token: 
#             stack.append(float(token))
#         else:  
#             b = stack.pop()
#             a = stack.pop()
#             if token == '+':
#                 stack.append(a + b)
#             elif token == '-':
#                 stack.append(a - b)
#             elif token == '*':
#                 stack.append(a * b)
#             elif token == '/':
#                 stack.append(a / b)

#     return stack.pop()

# print(evaluate_postfix("2 3 +"))
# print(evaluate_postfix("2 3 4 * +"))
# print(evaluate_postfix("10 5 / 2 +"))


#WAP to find second minimum and second maximum elements in a given list
#list=[1,3,7,4,11,6,1,0]
#Note- Other than len function you cannot use any ather function 


lst=[1,3,7,4,11,6,1,0]
print(type(lst))
for i in range(len(lst)):
    m=lst[i]
    for j in range(i,len(lst)):
        if lst[j]<m:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j] = m

print("second min num:",lst[1],"second max num:",lst[len(lst)-2])























