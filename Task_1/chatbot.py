
print("Welcome to DecodeLabs Rule-Based AI Chatbot!")
print("Type 'exit' or 'bye' to end the conversation.\n")

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What's on your mind?",
    "hey": "Hey! Great to see you. How's it going?",
    "how are you": "I'm doing great, thanks for asking! As a rule-based bot, I'm always ready. How about you?",
    "what is your name": "I'm ChatBot, your rule-based AI assistant from DecodeLabs.",
    "who are you": "I'm a simple rule-based chatbot built for the DecodeLabs AI training program.",
    "thank you": "You're welcome! Glad I could help.",
    "thanks": "No problem! Happy to assist.",
    "bye": "Goodbye! Have a wonderful day!",
    "goodbye": "Take care! See you next time.",
    "help": "I can respond to greetings, basic questions, and exit commands. Try saying 'hello' or 'how are you'!",
}

def get_response(user_input):
    """Process input and return appropriate response using dictionary lookup (O(1) average)."""
    cleaned = user_input.strip().lower()

    if cleaned in responses:
        return responses[cleaned]
    if "hello" in cleaned or "hi" in cleaned:
        return responses["hello"]
    if "how are you" in cleaned:
        return responses["how are you"]
    if "name" in cleaned:
        return responses["what is your name"]
    if "thank" in cleaned:
        return responses["thank you"]
    if "help" in cleaned:
        return responses["help"]
    return "I'm sorry, I didn't understand that. Try 'hello', 'how are you', or 'help' for more options."
while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() in ["exit", "bye", "goodbye", "quit"]:
        print("Bot: Goodbye! Thanks for chatting. See you in the next project! 👋")
        break
    
    response = get_response(user_input)
    print(f"Bot: {response}")