import random
import nltk 
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("wordnet")

lemmantizer = WordNetLemmatizer()

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "how are you"],
        "responses": ["Hello!", "Hi there!", "Hey, how can I help you!"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "reponses": ["Goodbye", "See you later", "Bye, Take care."]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses": ["Your welcome!", "No problem!", "Happy to help!"]
    }
}

def preprocess(text):
    #Tokenize and lemmatize
    tokens = nltk.word_tokenize(text.lower)
    tokens = [lemmantizer.lemmatize(token) for token in tokens]
    return tokens

#Finding the best matching intent
def get_intent(user_input):
    user_input = preprocess(user_input)
    best_match = None
    best_score = 0

    for intent_name, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            pattern_tokens = preprocess(pattern)
            #Counting common words
            score = len(set(user_input).intersection(set(pattern_tokens)))
            if score > best_score:
                best_score = score
                best_match = intent_name

    return best_match

#Chatbot function
def chatbot_response(user_input):
    intent = get_intent(user_input)
    if intent:
        return random.choice(intents[intent]["responses"])
    else:
        return "I am sorry, I do not understand that."
    
#Chatbot loop
exit_condition = ("q:", "quit","exit")
print("Chatbot: Hello! How can I help you today?(Type :q, quit or exit to end the chat.)")
case = True
while case == True:
    query = input("User: ")
    if query.lower() in exit_condition:
        break
    else:
        response = chatbot_response(query)
        print(f"Chatbot: {response}")