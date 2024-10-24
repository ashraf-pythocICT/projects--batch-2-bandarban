def chatbot():
    print("Hello! I'm a simple chatbot from batch-2. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if "hello" in user_input.lower():
            print("Chatbot: Hi there!")
        elif "how are you" in user_input.lower():
            print("Chatbot: I am good and hope you are also good.")
        elif "what is the name of your country" in user_input.lower():
            print("Chatbot: Bangladesh")
        elif "what class do you read in" in user_input.lower():
            print("Chatbot: class 8")
        elif "bye" in user_input.lower() or "exit" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")
            
chatbot()