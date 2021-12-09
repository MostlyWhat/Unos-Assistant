from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.logic import BestMatch, LogicAdapter
from chatterbot.response_selection import get_first_response
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("UNOS",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch", 
            "statement_comparison_function": LevenshteinDistance, 
            "response_selection_method": get_first_response
        },
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation"
        },
        {
            "import_path": "chatterbot.logic.TimeLogicAdapter"
        }
    ]
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
while True:
    trainer.train(
        "chatterbot.corpus.english"
        )
