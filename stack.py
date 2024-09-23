class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if not self.is_empty():
            print("Stack elements:", self.stack)
        else:
            print("Stack is empty")

stack = Stack()

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        element = input("Enter the element to push: ")
        stack.push(element)
        print(f"{element} pushed to stack.")
    elif choice == '2':
        popped_element = stack.pop()
        print(f"Popped element: {popped_element}")
    elif choice == '3':
        stack.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
