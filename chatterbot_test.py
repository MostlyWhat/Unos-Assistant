from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.logic import BestMatch
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.logic import LogicAdapter

chatbot = ChatBot("UNOS", 
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch", 
            "statement_comparison_function": LevenshteinDistance, 
            "response_selection_method": get_first_response
        }
    ]
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
    )

# Get a response to an input statement
user_input = input("Question: ")
response = str(chatbot.get_response(user_input))
print("Answer: " + response)