from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend",
])
trainer.train([
    "Are you a plant?",
    "No, I am the pot below the plant!",
])

exit_conditions = ("q:", "quit", "exit")
while True:
    query = input("User: ")
    if query in exit_conditions:
        break
    else:
        print(f"Chatpot: {chatbot.get_response(query)}")