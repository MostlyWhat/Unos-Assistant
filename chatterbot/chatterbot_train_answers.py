from chatterbot import ChatBot
from chatterbot.comparisons import SpacySimilarity
from chatterbot.conversation import Statement
from chatterbot.logic import BestMatch, LogicAdapter
from chatterbot.response_selection import get_first_response
from chatterbot.trainers import ChatterBotCorpusTrainer

"""
This example shows how to create a chat bot that
will learn responses based on an additional feedback
element from the user.
"""

# Uncomment the following line to enable verbose logging
import logging

logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot("UNOS",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.MathematicalEvaluation"
            },
            {
                "import_path": "chatterbot.logic.BestMatch", 
                "statement_comparison_function": SpacySimilarity, 
                "response_selection_method": get_first_response,
                'maximum_similarity_threshold': 0.90,
                'default_response': "I'm sorry, but I don't understand the question"
            }
        ]
    )


def get_feedback():

    text = input("Correct? (yes/no): ")

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Correct? (yes/no): ')
        return get_feedback()


print('UNOS Training System Version 1.0')

# The following loop will execute each time the user enters input
while True:
    try:
        input_statement = Statement(text=input("Question: "))
        response = bot.generate_response(
            input_statement
        )

        print(f"Answer: {response.text}")
        if get_feedback() is False:
            correct_response = Statement(text=input("Correct Response: "))
            bot.learn_response(correct_response, input_statement)
            print('Trainer: Response Added to UNOS')

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
