import nltk
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are downloaded
nltk.download('punkt')

# Define keyword-response pairs
responses = {
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there! How's it going?",
    "hey": "Hey! What’s up?",
    "bye": "Goodbye! Have a great day!"
}

def preprocess_text(text):
    """Tokenizes and lowers text for better pattern matching."""
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    return tokens

def chatbot_response(user_input):
    """Checks for keyword matches and returns the best response."""
    tokens = preprocess_text(user_input)

    # Check if any token is in the responses dictionary
    for word in tokens:
        if word in responses:
            return responses[word]

    return "I'm not sure how to respond to that. Could you ask something else?"

# Simple chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break
    print("Chatbot:", chatbot_response(user_input))
