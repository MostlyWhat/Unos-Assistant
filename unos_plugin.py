#Modules Importer
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import speech_recognition as record
import pyttsx3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import os
import random

class UNOS:
    #Run the initial settings
    def __init__(self):
        self.UNOSinitialize()

    def UNOSinitialize(self):
        #Make Variables Global
        global speech
        global recognizer
        global mic
        global API_KEY
        global WAKE
        global WAKEUP_COMMANDS
        global EXIT_COMMANDS

        #Main Configurations
        API_KEY = "AIzaSyDQuH9vvuKi9fL9KD8VWzDX2_p5G24UJQo"

        #Voice Commands
        WAKE = "hey john"
        WAKEUP_COMMANDS = ["uno's", "who knows", "nos", "nose", "hey Uno's", "hey who knows", "hey nos", "hey nose"]
        EXIT_COMMANDS = ["exit", "quit", "log off", "log out", "sign out"]

        #Initilisation of Recognition Systems
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
        os.system('cls' if os.name == 'nt' else 'clear')

        boot_sequence = open("boot_sequence.txt")
        boot_text = boot_sequence.readlines()
        for line in boot_text:
            print(line, end="")
            time.sleep(random.uniform(0,0.25))
        
        print("""
        
        Boot Complete

        """)
        time.sleep(5)

        os.system('cls' if os.name == 'nt' else 'clear')
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

    #Saying Speech
    def speak(self, text):
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
            #To use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            user_response = recognizer.recognize_google(audio)

            if user_response.lower() == WAKE:
                return "True"

            else:
                return str(user_response.lower())

        except record.UnknownValueError:
            return "UnknownValueError"

        except record.RequestError as e:
            return "RequestError"

    def RecognizeAudio(self):
        #Recognition of Voice Commands
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            #To use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            user_response = recognizer.recognize_google(audio)

            return str(user_response.lower())

        except record.UnknownValueError:
            return "UnknownValueError"

        except record.RequestError as e:
            return "RequestError"

    def runningCommand(self):
        print("UNOS: Command Please!")
        self.speak("Command Please!")
        command = self.RecognizeAudio()

        for exit_commands in EXIT_COMMANDS:
            if exit_commands in command:
                exit()

            else:
                print("UNOS: ERROR ( Reason: I don't understand the command )")