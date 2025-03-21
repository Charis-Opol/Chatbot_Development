import random
import nltk
from nltk.stem import WordNetLemmatizer
from faker import Faker  # Install with: pip install faker

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
fake = Faker()

# --- Original Static Intents (Fixed Typos) ---