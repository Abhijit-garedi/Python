def interactive_program():
    print("Welcome to the interactive program! Type 'exit' to quit.")
    while True:
        user_input = input("Enter your command or input: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
           #input output process
            print(f"You entered: {user_input}")


interactive_program()
