import json
import os
import pickle
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Disable Tensorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model

# Setting Up Configurations
config = Config()
crisis = Crisis()

# Setting Up Modules
lemmatizer = WordNetLemmatizer()
words = pickle.load(open(f'{config.words_lib}', 'rb'))
classes = pickle.load(open(f'{config.classes_lib}', 'rb'))

try:
    intents = json.loads(open(f"{config.mcas_dataset}").read())

# Except File Not Found Error 
except Exception as e:
    with open(f"{config.default_dataset}", "r") as default_dataset, open(f"{config.mcas_dataset}", "w") as mcas_dataset:
        mcas_dataset.write(default_dataset.read())
    intents = json.loads(open(f"{config.mcas_dataset}").read())

# Fallback Plugin for Splitter System

class Plugin:
    def __init__(self):
        self.name = "MCAS"
        self.contexts = []

    @staticmethod
    def analyze(query):
        # Set to True because we want to use the fallback module
        return True

    @staticmethod
    def clean_up_sentence(sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(
            word) for word in sentence_words]
        return sentence_words

    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    def process(self, query):
        bow = self.bag_of_words(query)

        core1 = self.Core1(bow)
        core2 = self.Core2(bow)
        core3 = self.Core3(bow)

        tag1 = core1[0]['intent']
        tag2 = core2[0]['intent']
        tag3 = core3[0]['intent']

        accuracy1 = float(core1[0]['probability'])
        accuracy2 = float(core2[0]['probability'])
        accuracy3 = float(core3[0]['probability'])

        # Check if all cores has accuracy more than 50%
        if accuracy1 >= 0.9 or accuracy2 >= 0.9 or accuracy3 >= 0.9:
            crisis.log("MCAS", "Pass Accuracy Value of 50%")
            crisis.log(
                f"{config.mcas_core1_name}", f"Selected {tag1} with a confidence of {accuracy1}")
            crisis.log(
                f"{config.mcas_core2_name}", f"Selected {tag2} with a confidence of {accuracy2}")
            crisis.log(
                f"{config.mcas_core3_name}", f"Selected {tag3} with a confidence of {accuracy3}")
            list_of_intents = intents['intents']
            
            # All Agree
            if tag1 == tag2 == tag3:
                crisis.log("MCAS", "All Agree")
                for i in list_of_intents:
                    if i['tag'] == tag1:
                        result = random.choice(i['responses'])
                        break

            elif tag1 != tag2 != tag3:
                crisis.log("MCAS", "All Disagree")
                values = {"tag1": accuracy1,
                          "tag2": accuracy2, "tag3": accuracy3}
                highest = max(values, key=values.get)

                if highest == "tag1":
                    crisis.log(
                        "MCAS", f"Core 1 has highest value of {accuracy1}")
                    for i in list_of_intents:
                        if i['tag'] == tag1:
                            result = random.choice(i['responses'])
                            break

                elif highest == "tag2":
                    crisis.log(
                        "MCAS", f"Core 2 has highest value of {accuracy2}")
                    for i in list_of_intents:
                        if i['tag'] == tag2:
                            result = random.choice(i['responses'])
                            break

                else:
                    crisis.log(
                        "MCAS", f"Core 3 has highest value of {accuracy3}")
                    for i in list_of_intents:
                        if i['tag'] == tag1:
                            result = random.choice(i['responses'])
                            break

            else:
                crisis.log(
                    "MCAS", "2 Cores Agree and 1 Core Disagree")
                if tag1 == tag2:
                    crisis.log(
                        "MCAS", "Core 1 and 2 Agree")
                    for i in list_of_intents:
                        if i['tag'] == tag1:
                            result = random.choice(i['responses'])
                            break

                elif tag2 == tag3:
                    crisis.log(
                        "MCAS", "Core 2 and 3 Agree")
                    for i in list_of_intents:
                        if i['tag'] == tag2:
                            result = random.choice(i['responses'])
                            break

                elif tag1 == tag3:
                    crisis.log(
                        "MCAS", "Core 1 and 3 Agree")
                    for i in list_of_intents:
                        if i['tag'] == tag3:
                            result = random.choice(i['responses'])
                            break

        else:
            crisis.log("MCAS", "Failed Accuracy Value of 50%")
            crisis.log(
                f"{config.mcas_core1_name}", f"Selected {tag1} with a confidence of {accuracy1}")
            crisis.log(
                f"{config.mcas_core2_name}", f"Selected {tag2} with a confidence of {accuracy2}")
            crisis.log(
                f"{config.mcas_core3_name}", f"Selected {tag3} with a confidence of {accuracy3}")
            
            # Returns the Unknown Intent as Answer
            list_of_intents = intents['intents']
            for i in list_of_intents:
                if i['tag'] == "unknown":
                    result = random.choice(i['responses'])

        return result

    @staticmethod
    def Core1(bow):
        # SkyNET Core
        model = load_model(config.mcas_core1)
        res = model.predict(np.array([bow]))[0]
        results = [[i, r] for i, r in enumerate(res)]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

    @staticmethod
    def Core2(bow):
        # Strik3r Core
        model = load_model(config.mcas_core2)
        res = model.predict(np.array([bow]))[0]
        results = [[i, r] for i, r in enumerate(res)]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

    @staticmethod
    def Core3(bow):
        # Steve Core
        model = load_model(config.mcas_core2)
        res = model.predict(np.array([bow]))[0]
        results = [[i, r] for i, r in enumerate(res)]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
