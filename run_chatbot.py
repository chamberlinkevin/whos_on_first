from Abbott_and_Costello import WhosOnFirstChatbot

def run_chatbot():
    bot = WhosOnFirstChatbot()
    print("Welcome to the 'Who's on First?' Chatbot!")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_chatbot()