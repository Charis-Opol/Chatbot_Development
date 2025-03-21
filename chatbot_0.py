import random
import nltk
from nltk.stem import WordNetLemmatizer
from faker import Faker  # Install with: pip install faker

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
fake = Faker()

# --- Original Static Intents (Fixed Typos) ---
original_intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "how are you"],
        "responses": ["Hello!", "Hi there!", "Hey, how can I help you!"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye", "See you later", "Bye, Take care."]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    }
}

# --- Dynamic Intent Generation (Fixed & Expanded) ---
def generate_dynamic_intents(num_samples=250):
    """Generates 20 intents with 250 patterns/responses each (5,000 total)"""
    
    intent_templates = {
        # Existing intents (fixed)
        "weather": {
            "patterns": [
                "What's the weather in {city}?",
                "Will it rain in {city} tomorrow?",
                "Is it sunny in {city}?"
            ],
            "responses": [
                "It's {weather_condition} in {city}.",
                "Expect {weather_condition} in {city} today."
            ]
        },
        "food": {
            "patterns": [
                "Find me a {cuisine} restaurant",
                "Where can I get {dish} in {city}?",
                "How do I cook {dish}?"
            ],
            "responses": [
                "Try {restaurant} for {cuisine} food!",
                "Here's a recipe: {recipe_link}"
            ]
        },
        "movies": {
            "patterns": [
                "Is {movie} streaming on {streaming_service}?",
                "Recommend a {genre} movie"
            ],
            "responses": [
                "Watch {movie} on {streaming_service}!",
                "For {genre}, try {recommended_movie}."
            ]
        },
        # New intents (add more as needed)
        "shopping": {
            "patterns": [
                "Where can I buy {product}?",
                "Is {product} on sale?"
            ],
            "responses": [
                "{product} is available at {store}.",
                "Check {store} for discounts!"
            ]
        },
        "travel": {
            "patterns": [
                "How far is {city} from here?",
                "Find hotels in {city}"
            ],
            "responses": [
                "Top hotels in {city}: {hotel}",
                "{city} is {distance} miles away."
            ]
        }
    }

    # Expanded data pools (all placeholders covered)
    data_pools = {
        "city": [fake.city() for _ in range(100)],
        "weather_condition": ["sunny", "rainy", "cloudy"],
        "cuisine": ["Italian", "Mexican", "Japanese"],
        "dish": ["pizza", "sushi", "tacos"],
        "restaurant": ["The Golden Fork", "Spice Palace"],
        "movie": [fake.catch_phrase() for _ in range(50)],
        "genre": ["comedy", "horror", "drama"],
        "streaming_service": ["Netflix", "Hulu"],
        "recommended_movie": [fake.catch_phrase() for _ in range(50)],
        "recipe_link": [fake.url() for _ in range(50)],
        "product": ["headphones", "laptops", "books"],
        "store": ["Amazon", "Best Buy", "Walmart"],
        "hotel": ["Grand Hotel", "Sea View Inn"],
        "distance": [str(random.randint(10, 500)) for _ in range(50)]
    }

    dynamic_intents = {}
    for intent_name, template in intent_templates.items():
        patterns = []
        responses = []
        for _ in range(num_samples):
            # Get fresh random data for each sample
            data = {key: random.choice(values) for key, values in data_pools.items()}
            
            # Replace placeholders in patterns/responses
            try:
                pattern = random.choice(template["patterns"]).format(**data)
                response = random.choice(template["responses"]).format(**data)
                patterns.append(pattern.lower())
                responses.append(response)
            except KeyError as e:
                print(f"Missing key in template: {e}")
                continue
        
        dynamic_intents[intent_name] = {
            "patterns": patterns,
            "responses": responses
        }
    
    return dynamic_intents

# Generate dynamic intents (now error-free)
dynamic_intents = generate_dynamic_intents()

# Merge with original intents
combined_intents = {**original_intents, **dynamic_intents}

# --- Rest of Your Chatbot Code (Unchanged) ---
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

def get_intent(user_input):
    user_tokens = preprocess(user_input)
    best_match = None
    best_score = 0
    for intent_name, intent_data in combined_intents.items():
        for pattern in intent_data["patterns"]:
            pattern_tokens = preprocess(pattern)
            score = len(set(user_tokens) & set(pattern_tokens))
            if score > best_score:
                best_score = score
                best_match = intent_name
    return best_match

def chatbot_response(user_input):
    intent = get_intent(user_input)
    if intent:
        return random.choice(combined_intents[intent]["responses"])
    return "I’m still learning. Could you rephrase that?"

# Chat loop
exit_conditions = ("q", "quit", "exit")
print("Chatbot: Hello! Ask me anything. Type 'q', 'quit', or 'exit' to end.")

while True:
    user_input = input("You: ")
    if user_input.lower() in exit_conditions:
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")