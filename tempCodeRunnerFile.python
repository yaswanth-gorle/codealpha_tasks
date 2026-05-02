def get_response(user_input):
    """Return a predefined reply based on user input."""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hi there! 👋 How can I help you?"

    elif user_input in ["how are you", "how are you?", "how r u"]:
        return "I'm doing great, thanks for asking! 😊"

    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "I'm ChatBot, your simple Python assistant! 🤖"

    elif user_input in ["what can you do", "help", "help me"]:
        return "I can respond to greetings, answer basic questions, and chat with you!"

    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Sorry, I didn't understand that. Try saying 'hello' or 'help'!"


def run_chatbot():
    """Main loop to run the chatbot."""
    print("=" * 40)
    print("       Welcome to Python ChatBot!       ")
    print("  Type 'bye' or 'exit' to quit the bot  ")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please type something!")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        
        if user_input.lower() in ["bye", "goodbye", "see you", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()