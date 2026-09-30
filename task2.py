def chatbot():
    print("Alpha Bot: Hello! I am a simple chatbot.")
    print("Alpha Bot: Type 'help' to see what I can do.")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello" or user == "hi" or user == "hey" or user == "hey there":
            print("Alpha Bot: Hi! Nice to meet you.")

        elif user == "how are you" or user == "how are you doing":
            print("Alpha Bot: I'm fine, thanks!")

        elif user == "what is your name" or user == "what's your name":
            print("Alpha Bot: My name is Alpha Bot.")

        elif user == "who are you":
            print("Alpha Bot: I am a simple rule-based chatbot.")

        elif user == "help":
            print("Alpha Bot: You can ask me things like:")
            print("Alpha Bot: hello")
            print("Alpha Bot: how are you")
            print("Alpha Bot: what is your name")
            print("Alpha Bot: tell me a joke")
            print("Alpha Bot: thanks")
            print("Alpha Bot: bye")
            print("Alpha Bot: who created you")

        elif user == "who created you":
            print("Alpha Bot: I was created by a programmer, Jashwanth.")

        elif user == "thanks" or user == "thank you":
            print("Alpha Bot: You're welcome!")

        elif user == "good morning":
            print("Alpha Bot: Good morning! Have a great day.")

        elif user == "good afternoon":
            print("Alpha Bot: Good afternoon!")

        elif user == "good evening":
            print("Alpha Bot: Good evening!")

        elif user == "what can you do":
            print("Alpha Bot: I can have a simple conversation with you.")

        elif user == "tell me a joke":
            print("Alpha Bot: Why did the computer go to the doctor?")
            print("Alpha Bot: Because it had a virus!")

        elif user == "what is python":
            print("Alpha Bot: Python is a popular programming language.")

        elif user == "i like python":
            print("Alpha Bot: That's great! Python is fun to learn.")

        elif user == "are you real":
            print("Alpha Bot: No, I am a computer program.")

        elif user == "are you a robot":
            print("Alpha Bot: Yes, you can think of me as a simple chatbot.")

        elif user == "bye" or user == "goodbye" or user == "see you":
            print("Alpha Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Alpha Bot: Sorry, I don't understand that.")
            print("Alpha Bot: Type 'help' to see the available commands.")


chatbot()