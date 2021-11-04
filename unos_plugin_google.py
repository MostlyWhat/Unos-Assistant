#Modules Importer
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from google.cloud import speech as record
import pyttsx3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import os
import random
import json


class UNOS:
    #Run the initial settings
    def __init__(self):
        self.UNOSinitialize()

    def UNOSinitialize(self):
        #Make Variables Global
        global speech
        global recognizer
        global mic
        global config
        global API_KEY
        global GOOGLE_CLOUD_SPEECH_CREDENTIALS
        global WAKE
        global WAKEUP_COMMANDS
        global INTRO_COMMANDS
        global EXIT_COMMANDS
        global INTRO_RESPONSE

        #Main Configurations
        API_KEY = ""
        config = dict(language_code="en-US")

        #Start Voice Commands
        WAKE = "hey uno's"
        WAKEUP_COMMANDS = ["uno's", "who knows", "nos", "nose", "hey Uno's", "hey who knows", "hey nos", "hey nose"]
        INTRO_COMMANDS = ["hello", "hi", "",]
        EXIT_COMMANDS = ["exit", "quit", "log off", "log out", "sign out"]

        #Response Voice Command
        INTRO_RESPONSE = ["hello", "greetings", "hi", "bon jour", "ello", "hello there"]

        #Initilisation of Recognition Systems
        speech = pyttsx3.init()
        recognizer = speech.SpeechClient()
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

          ___           ___           ___           ___     
         /\__\         /\__\         /\  \         /\  \    
        /:/  /        /::|  |       /::\  \       /::\  \   
       /:/  /        /:|:|  |      /:/\:\  \     /:/\ \  \  
      /:/  /  ___   /:/|:|  |__   /:/  \:\  \   _\:\~\ \  \ 
     /:/__/  /\__\ /:/ |:| /\__\ /:/__/ \:\__\ /\ \:\ \ \__\
     \:\  \ /:/  / \/__|:|/:/  / \:\  \ /:/  / \:\ \:\ \/__/
      \:\  /:/  /      |:/:/  /   \:\  /:/  /   \:\ \:\__\  
       \:\/:/  /       |::/  /     \:\/:/  /     \:\/:/  /  
        \::/  /        /:/  /       \::/  /       \::/  /   
         \/__/         \/__/         \/__/         \/__/    

    [ UNIFIED NON-INTELLIGENT-ASSISTANT OPEN-SOURCED SYSTEM ]

    Name: U.N.O.S
    Version: 0.2.1-alpha
    Codename: Ultron
    Status: Unstable
    Previous Interation: SKYNET v0.1.1-alpha

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
            audio = 

        try:
            #To use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            user_response = recognizer.recognize(config=config, audio=source)

            if WAKEUP_COMMANDS.count(user_response.lower()) > 0:
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
            user_response = recognizer.recognize_google(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)

            return str(user_response.lower())

        except record.UnknownValueError:
            return "UnknownValueError"

        except record.RequestError as e:
            return "RequestError"

    def runningCommand(self):
        print("UNOS: Command Please!")
        self.speak("Command Please!")
        command = self.RecognizeAudio()

        for intro_commands in INTRO_COMMANDS:
            if intro_commands in command:
                print("UNOS: Detected Greetings, Responding")
                self.speak(random.choice(INTRO_RESPONSE))

                return None

        for exit_commands in EXIT_COMMANDS:
            if exit_commands in command:
                print("UNOS: Shutting Down System")
                self.speak("shutting down system")
                exit()