
print("Chatbot: Hello! I’m your friendly chatbot. Type 'bye' or 'quit' to exit.\n")

# Predefined response rules
responses = {
    "hello": ["Hello there!", "Hi! How can I assist you?"],
    "hi": ["Hi!", "Hey there!"],
    "how are you": ["I'm doing fine, thanks! How about you?", 
                    "All good here. You?"],
    "weather": ["I don't fetch real weather, but hope it's nice!", 
                "Weather's unknown—sorry!"],
    "joke": ["Why don't programmers like nature? Too many bugs!", 
             "Why do Java developers wear glasses? Because they don't C#!"],
    "python": ["Python is great for scripting, web, AI, and more!",
               "I love Python—what do you like about it?"],
    "thanks": ["You're welcome!", "No problem!"],
    "thank you": ["Glad to help!", "Anytime!"]
}

def get_response(user_input):
    inp = user_input.lower()
    # exact match
    if inp in ("bye", "quit", "exit"):
        return "Goodbye! It was nice talking to you.", True
    
    for key, replies in responses.items():
        if key in inp:
            import random  # internal optional import
            return random.choice(replies), False

    # fallback
    return ("I’m not sure I understand. "
            "You can ask me about Python, weather, tell a joke, etc."), False

# Chat loop
while True:
    user = input("You: ").strip()
    reply, exit_flag = get_response(user)
    print("Chatbot:", reply)
    if exit_flag:
        break
