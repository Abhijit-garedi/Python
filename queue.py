# program using queue > pop push display

class Queue:
    def __init__(self):
        self.queue = []
    
    # Push: Enqueue an element
    def push(self, item):
        self.queue.append(item)
        print(f"Item {item} pushed to the queue.")
    
    # Display: Show all elements in the queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print("Queue elements:", self.queue)


# Example usage:
q = Queue()

while True:
    user_input = input("Enter an element to push to the queue (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    q.push(user_input)

q.display()




