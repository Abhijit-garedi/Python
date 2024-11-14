# Stack Implementation using list
stack = []

# Push an element to the stack
def push(element):
    stack.append(element)
    print(f"Pushed {element} to stack")

# Pop an element from the stack
def pop():
    if not stack:
        print("Stack is empty")
        return None
    return stack.pop()

# Peek the top element of the stack
def peek():
    if not stack:
        print("Stack is empty")
        return None
    return stack[-1]

# Testing stack operations
push(10)
push(20)
push(30)
print("Top element:", peek())  
print("Popped element:", pop())  
print("Stack after pop:", stack) 

#output
# Pushed 10 to stack
# Pushed 20 to stack
# Pushed 30 to stack
# Top element: 30
# Popped element: 30
# Stack after pop: [10, 20]
