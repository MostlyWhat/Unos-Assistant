import json
import os
import pickle
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from System.Modules.BootLoader import Config
from tensorflow.keras.models import load_model

# Disable Tensorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Setting Up Configurations
config = Config()

# Setting Up Modules
lemmatizer = WordNetLemmatizer()
intents = json.loads(open(f"{config.default_dataset}").read())
words = pickle.load(open(f'{config.words_lib}', 'rb'))
classes = pickle.load(open(f'{config.classes_lib}', 'rb'))

# Fallback Plugin


class Plugin:
    def __init__(self):
        self.name = "System.Analysis.MCAS"
        self.contexts = []

    def analyze(self, query):
        # Some prints to identify which plugin is been used
        # True
        return True

    def clean_up_sentence(self, sentence):
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

        try:
            tag1 = core1[0]['intent']
            tag2 = core2[0]['intent']
            tag3 = core3[0]['intent']

            accuracy1 = float(core1[0]['probability'])
            accuracy2 = float(core2[0]['probability'])
            accuracy3 = float(core3[0]['probability'])

        except Exception as e:
            print(e)
            accuracy1 = float(0)
            accuracy2 = float(0)
            accuracy3 = float(0)

        # Check if all cores has accuracy more than 50%
        if accuracy1 > 0.5 or accuracy2 > 0.5 or accuracy3 > 0.5:
            print("MCAS: Pass Accuracy Value of 25%")
            print(
                f"SkyNET has selected {tag1} with a confidence of {accuracy1}")
            print(
                f"Strik3r has selected {tag2} with a confidence of {accuracy2}")
            print(
                f"Steve has selected {tag3} with a confidence of {accuracy3}")
            list_of_intents = intents['intents']
            # All Agree
            if tag1 == tag2 == tag3:
                print("MCAS: All Agree")
                for i in list_of_intents:
                    if i['tag'] == tag1:
                        result = random.choice(i['responses'])
                        break

            elif tag1 != tag2 != tag3:
                print("MCAS: All Disagree")
                values = {"tag1": accuracy1,
                          "tag2": accuracy2, "tag3": accuracy3}
                highest = max(values, key=values.get)

                if highest == "tag1":
                    print(f"MCAS: Core 1 has highest value of {accuracy1}")
                    for i in list_of_intents:
                        if i['tag'] == tag1:
                            result = random.choice(i['responses'])
                            break

                elif highest == "tag2":
                    print(f"MCAS: Core 2 has highest value of {accuracy2}")
                    for i in list_of_intents:
                        if i['tag'] == tag2:
                            result = random.choice(i['responses'])
                            break

                else:
                    print(f"MCAS: Core 3 has highest value of {accuracy3}")
                    for i in list_of_intents:
                        if i['tag'] == tag1:
                            result = random.choice(i['responses'])
                            break

            else:
                print("MCAS: 2 Agree")
                if tag1 == tag2:
                    print("MCAS: Core 1 & 2 has agree")
                    for i in list_of_intents:
                        if i['tag'] == tag1:
                            result = random.choice(i['responses'])
                            break

                elif tag2 == tag3:
                    print("MCAS: Core 2 & 3 has agree")
                    for i in list_of_intents:
                        if i['tag'] == tag2:
                            result = random.choice(i['responses'])
                            break

                else:
                    print("MCAS: Core 1 & 3 has agree")
                    for i in list_of_intents:
                        if i['tag'] == tag3:
                            result = random.choice(i['responses'])
                            break

        else:
            print("MCAS: Failed Accuracy Value of 50%")
            print(
                f"SkyNET has selected {tag1} with an confidence of {accuracy1}")
            print(
                f"Strik3r has selected {tag2} with an confidence of {accuracy2}")
            print(
                f"Steve has selected {tag3} with an confidence of {accuracy3}")
            not_found = ["I cannot answer that", "Different Question Please"]
            result = random.choice(not_found)

        return result

    def Core1(self, bow):
        # SkyNET Core
        model = load_model(config.MCAS_core1)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

    def Core2(self, bow):
        # Strik3r Core
        model = load_model(config.MCAS_core2)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

    def Core3(self, bow):
        # Steve Core
        model = load_model(config.MCAS_core2)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
