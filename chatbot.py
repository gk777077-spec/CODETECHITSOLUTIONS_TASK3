import nltk
import random

# Auto-download 'punkt' if not available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.tokenize import word_tokenize

# Intent response database
responses = {
    "greeting": [
        "Hi there!", "Hello!", "Hey!", "Hi, how can I assist you?"
    ],
    "goodbye": [
        "Bye!", "Goodbye!", "See you later!", "Take care!"
    ],
    "thanks": [
        "You're welcome!", "No problem!", "Glad to help!"
    ],
    "about": [
        "I am an AI chatbot created using Python and NLTK.",
        "I was built to respond to your questions using simple NLP techniques."
    ],
    "capabilities": [
        "I can chat with you, answer basic questions, and help demonstrate NLP!",
        "I can recognize greetings, questions, and respond with useful info."
    ],
    "default": [
        "I'm not sure I understand. Could you try rephrasing?",
        "Hmm, I didn't catch that. Can you ask another way?",
        "I’m still learning. Try asking something else!"
    ]
}

# Keywords for matching intent
keywords = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "exit", "see you", "farewell"],
    "thanks": ["thanks", "thank you", "thx", "much appreciated"],
    "about": ["who are you", "what are you", "tell me about yourself", "your name"],
    "capabilities": ["what can you do", "help", "your features", "abilities", "functions"]
}

# Detect intent based on keywords or phrases
def get_intent(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for intent, key_list in keywords.items():
        for word in tokens:
            if word in key_list:
                return intent
        for phrase in key_list:
            if phrase in user_input:
                return intent
    return "default"

# Generate response
def get_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# Main chatbot loop
print("🤖 Chatbot is ready! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("🤖:", random.choice(responses["goodbye"]))
        break
    response = get_response(user_input)
    print("🤖:", response)
