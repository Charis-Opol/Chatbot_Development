import re
import random

# Define patterns and responses
patterns = [
    (r"i need (.*)", [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ]),
    (r"why don\'?t you ([^\?]*)\??", [
        "Do you really think I don't {0}?",
        "Perhaps eventually I will {0}.",
        "Do you really want me to {0}?"
    ]),
    (r"i\'?m (.*)", [
        "How does being {0} make you feel?",
        "Do you enjoy being {0}?",
        "Why do you think you're {0}?"
    ]),
    (r"i feel (.*)", [
        "Why do you feel {0}?",
        "How long have you been feeling {0}?",
        "Do you often feel {0}?"
    ]),
    (r"i am (.*)", [
        "Why are you {0}?",
        "How does being {0} make you feel?",
        "Do you enjoy being {0}?"
    ]),
    (r"how (.*)", [
        "Why do you ask?",
        "How would an answer to that help you?",
        "What do you think?"
    ]),
    (r"because (.*)", [
        "Is that the real reason?",
        "What other reasons come to mind?",
        "Does that reason apply to anything else?"
    ]),
    (r"(.*) sorry (.*)", [
        "There's no need to apologize.",
        "What feelings do you have when you apologize?",
        "Why are you sorry?"
    ]),
    (r"hi|hello|hey", [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! How are you feeling?"
    ]),
    (r"quit", [
        "Goodbye! Take care.",
        "It was nice talking to you. Bye!",
        "Farewell! Feel free to come back anytime."
    ]),
    (r"(.*)", [
        "Can you elaborate on that?",
        "Why do you say that?",
        "How does that make you feel?"
    ])
]

def eliza_response(user_input):
    """Generate a response based on user input."""
    for pattern, responses in patterns:
        print(pattern)
        match = re.match(pattern, user_input.lower())
        print(match)
        if match:
            response = random.choice(responses)
            print(response)
            return response.format(*match.groups())
    return "I'm not sure how to respond to that."

def chat():
    """Run the ELIZA chatbot."""
    print("ELIZA: Hello! I'm ELIZA, your therapist. How can I help you today? (Type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ELIZA: Goodbye! Take care.")
            break
        response = eliza_response(user_input)
        print(f"ELIZA: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()