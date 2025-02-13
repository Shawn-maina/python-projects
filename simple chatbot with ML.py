import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm just a bot, but I'm doing fine!", "I'm great! How about you?"],
        "bye": ["Goodbye!", "See you later!", "Have a great day!"]
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
