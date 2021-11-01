#Modules Importer
import speech_recognition as record
import pyttsx3
import sys
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import os

class UNOS:
    #Run the initial settings
    def __init__(self):
        self.UNOSinitialize()

    def UNOSinitialize(self):
        #Main Configurations


        #Initilisation of Recognition Systems
        global speech
        global recognizer
        global mic

        speech = pyttsx3.init()
        recognizer = record.Recognizer()
        mic = record.Microphone()

    #Verification Before Launch
    def Verify(self):
        continue_flag = input("Warning! UNOS is unstable in it's current state. Are you sure you want to continue? (y/N): ")

        if continue_flag == "y":
            print("Launching UNOS")
            time.sleep(3)
            return "True"

        else:
            print("Program Closing")
            time.sleep(3)
            return "False"

    #Startup Text
    def StartupText(self):
        print("""
        [ UNIFIED NON-INTELLIGENT-ASSISTANT OPEN-SOURCED SYSTEM ]

        Name: U.N.O.S
        Version: 0.0.1-alpha
        Codename: Ultron
        Status: Unstable
        """)
        print("UNOS: System Ready for Inquiry")
        speech.say("System is ready for Inquiry")
        speech.runAndWait()
        time.sleep(2)

    #Saying Speech
    def speak(text):
        speech.say(text)
        speech.runAndWait()

    #Main User Interface Loop
    def MainWindow():
        #SettingUpWindow
        qapp = QApplication(sys.argv)
        window = QMainWindow()
        window.setGeometry(200,200,300,300) # sets the windows x, y, width, height
        window.setWindowTitle("UNOS Assistant Version 0.1 (Not Production Ready)") # setting the window title

        label = QLabel(window)
        label.setText("my first label")
        label.move(50, 50) 

        window.showMaximized()
        sys.exit(qapp.exec_())

    def RecognizeUNOS(self):
        #Recognition of Voice Commands
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            # For testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            user_response = recognizer.recognize_google(audio)

            if user_response == "Uno's" or "who knows" or "nos" or "nose":
                return "True"

            else:
                return "False"

        except record.UnknownValueError:
            return "UnknownValueError"

        except record.RequestError as e:
            return "RequestError"

    def RecognizeCommand(self):
        #Recognition of Voice Commands
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            # For testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            user_response = recognizer.recognize_google(audio)

            return user_response  

        except record.UnknownValueError:
            return "UnknownValueError"

        except record.RequestError as e:
            return "RequestError"