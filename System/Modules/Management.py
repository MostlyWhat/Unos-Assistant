import json
import os
import pickle
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD

# Module Information
# Module Name: System.Modules.Trainer
# Module Purpose: To Provide the Training for the AI System of UNOS Assistant Framework such as MCAS and SCAS

"""
General Idea:

For Libaries Regneration: ex manager regenerate libaries
1. Reads the default.json or other database from config.default_dataset
2. Generate Classes and Words Libraries to Data/Library/Classes.pk1 and Data/Library/Words.pk1

For MCAS Regnerate the Core 1, Core 2 and Core 3: ex trainer retrain MCAS
3. Checks for Training Configuration
4. Run 
"""

# Setting Up Modules
config = Config()
crisis = Crisis()
lemmatizer = WordNetLemmatizer()

# Setting Up Configurations
lemmatizer = WordNetLemmatizer()
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']
training = []

# Load Database
try:
    intents = json.loads(open(f"{config.mcas_dataset}").read())

# Except File Not Found Error 
except Exception as e:
    intents = json.loads(open(f"{config.default_dataset}").read())

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word)
         for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(
        word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

class Updater():
    def regen(self, database):
        if database == "libaries":            
            try:
                if os.path.exists(f"{config.words_lib}"):
                    os.remove(f"{config.words_lib}")
                    
                if os.path.exists(f"{config.classes_lib}"):
                    os.remove(f"{config.classes_lib}")
                
                pickle.dump(words, open(f'{config.words_lib}', 'wb'))
                pickle.dump(classes, open(f'{config.classes_lib}', 'wb'))
                
                return True
            
            except Exception:
                return False
        
        elif database == "mcas":
            self.SkyNET_Training()
            self.Strik3r_Training()
            self.Steve_Training()
            
            return True
        
        elif database == "all":
            if os.path.exists(f"{config.words_lib}"):
                os.remove(f"{config.words_lib}")
                    
            if os.path.exists(f"{config.classes_lib}"):
                os.remove(f"{config.classes_lib}")
            
            pickle.dump(words, open(f'{config.words_lib}', 'wb'))
            pickle.dump(classes, open(f'{config.classes_lib}', 'wb'))
                
            self.SkyNET_Training()
            self.Strik3r_Training()
            self.Steve_Training()
            
            return True

        else:
            return False
    
    def SkyNET_Training(self):
        model = Sequential()
        model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu')) 
        model.add(Dropout(0.5)) 
        model.add(Dense(256, activation='relu')) 
        model.add(Dropout(0.5))
        model.add(Dense(len(train_y[0]), activation='softmax'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy',
                    optimizer=sgd, metrics=['accuracy'])

        hist = model.fit(np.array(train_x), np.array(train_y),
                        epochs=200, batch_size=5, verbose=1)
        
        if os.path.exists(f"{config.mcas_core1}"):
            os.remove(f"{config.mcas_core1}")
        
        model.save(f'{config.mcas_core1}', hist)
        
    def Strik3r_Training(self):
        model=Sequential()
        model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
        model.add(Dropout(0.5)) 
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5)) 
        model.add(Dense(len(train_y[0]), activation='softmax'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy',
                    optimizer=sgd, metrics=['accuracy'])

        hist = model.fit(np.array(train_x), np.array(train_y),
                        epochs=200, batch_size=5, verbose=1)
        
        if os.path.exists(f"{config.mcas_core2}"):
            os.remove(f"{config.mcas_core2}")
        
        model.save(f'{config.mcas_core2}', hist)
        
    def Steve_Training(self):
        model = Sequential() 
        model.add(Dense(64, input_shape=(len(train_x[0]),), activation='relu'))
        model.add(Dropout(0.5)) 
        model.add(Dense(32, activation='relu'))
        model.add(Dropout(0.5)) 
        model.add(Dense(16, activation='relu'))
        model.add(Dropout(0.5)) 
        model.add(Dense(len(train_y[0]), activation='softmax'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy',
                    optimizer=sgd, metrics=['accuracy'])

        hist = model.fit(np.array(train_x), np.array(train_y),
                        epochs=200, batch_size=5, verbose=1)
        
        if os.path.exists(f"{config.mcas_core3}"):
            os.remove(f"{config.mcas_core3}")
        
        model.save(f'{config.mcas_core3}', hist)

class Autofixer:
    pass
