#Queue - First in First Out(FIFO)

#WAP to implement basic queue with the help of queue with the method names as 
# DQ,NQ is_peekelement,is_empty and length


# #Implement queue using list
# queue = []

# #Enqueue
# queue.append('A')
# queue.append('B')
# queue.append('C')

# #Dequeue
# poppedElement=queue.pop(0)
# print("Dequeue:",poppedElement)

# #Peek Value
# frontElement=queue[0]
# print("Peek:",frontElement)

# #isEmpty
# isempty=not bool(queue)
# print("isEmpty",isempty)

# #size or Length
# print("Size:",len(queue))


#Q2) WAP to implement CPU task management system using linear data structure where
#consider 3 task. All the 3 task should execute one after the other considering 
# FIFO principle
#a) With sleep Method
#b) Without sleep Method
#Hint: Use sleep method to pause the operation


# CPU = []

# def cpu_task_mang(task_management):
#     tokens = task_management.split()

#     for token in tokens:
#         if token.isdigit(): 
#             CPU.append(int(token))
#         elif '.' in token: 
#             CPU.append(float(token))
#         else:  
#             b = CPU.pop()
#             a = CPU.pop()
#             if token == '+':
#                 CPU.append(a + b)
#             elif token == '-':
#                 CPU.append(a - b)
#             elif token == '*':
#                 CPU.append(a * b)
#             elif token == '/':
#                 CPU.append(a / b)

#     return CPU.pop()

# print(cpu_task_mang("2 3 +"))
# print(cpu_task_mang("2 3 4 * +"))
# print(cpu_task_mang("10 5 / 2 +"))


class Task:
    def __init__(self,task_id,task_name,burst_time):
        self.task_id=task_id
        self.task_name=task_name
        self.burst_time=burst_time
    
    def __str__(self): #Method used to print the string
        print(self.task_id, self.task_name, self.burst_time)
        return f"TaskID:{self.task_id},Name:{self.task_name},Burst Time:{self.burst_time}"
    
#Create a task queue using List
task_queue=[]
#Add task method
def add_task(task_id,task_name,burst_time):
    task=Task(task_id,task_name,burst_time)
    task_queue.append(task)
    print(f"Task Added:{task}")
#Function execute tasks
def execute_tasks():
    print("\n--- execution tasks---\n")
    while(task_queue):
        task=task_queue[0]      #get the first task
        task_queue.pop(0)       #To remove from front
        print(f"Executing{task}")
        #sleep method
        time.sleep(task.burst_time)
        print(f"Completed :{task.task_name}\n")
        print("--ALL TASK COMPLETED--")
t=Task(1,"abc",2)
print(t)

#DBMS- DATA BASE MANAGEMENT SYSTEM
#DATA: 
















