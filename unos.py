#Modules Importer
import speech_recognition as record
import pyttsx3
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import UNOS

class UNOS:
    #Run the initial settings
    def __init__(self, *args, **kwargs):
        #Main Configurations
        activated = True #Toggle on/off
        unos = ChatBot('UNOS') #Name of the Assistant

        #Initilisation of Recognition Systems
        speech = pyttsx3.init()
        recognizer = record.Recognizer()
        mic = record.Microphone()

    #Verification Before Launch
    def Verify():
        continue_flag = input("Warning! UNOS is unstable in it's current state. Are you sure you want to continue? (y/N): ")

        if continue_flag == "y":
            print("Launching UNOS")
            time.sleep(3)
            UnosSystems()

        else:
            print("Program Closing")
            exit()

    #Startup Text
    def StartupText(self):
        print("""
        [ UNIFIED NON-INTELLIGENT-ASSISTANT OPEN-SOURCED SYSTEM ]

        Version: 0.1-alpha
        Codename: Ultron
        Status: Unstable
        """)
        print("UNOS: System Ready for Inquiry")

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

    def Recognition():
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
            print("UNOS: Recognised --> " + user_response)

            if user_response == "Uno's" or "who knows" or "nos" or "nose":
                speech.say("Hello Unknown User!")
                speech.runAndWait()    

            except record.UnknownValueError:
                print("UNOS: Error Recognising the Speech, Please Try Again")
                speech.say("Error Recognising the Speech, Please Try Again")
                speech.runAndWait()

            except record.RequestError as e:
                print("UNOS: Error Requesting Data From Google API; {0}".format(e))
                speech.say("Error Requesting Data From Google API, Is the internet connection is not available?")
                speech.runAndWait()