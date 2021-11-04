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
        global API_KEY
        global GOOGLE_CLOUD_SPEECH_CREDENTIALS
        global WAKE
        global WAKEUP_COMMANDS
        global INTRO_COMMANDS
        global EXIT_COMMANDS
        global INTRO_RESPONSE

        #Main Configurations
        API_KEY = "AIzaSyDQuH9vvuKi9fL9KD8VWzDX2_p5G24UJQo"
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{"type": "service_account","project_id": "persuasive-zoo-330804","private_key_id": "2e370ea964d728511eff9877eb8025887f7ba9f1","private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDSan6uWTxiDSPo\no1OeEHENBDZ3RHGUGiEARHkzdqESMg0oU1nnpaPCLQEq8Y6eBdEzzrmvyUc4ckFE\nSA9OzIMvOARkKFU6IKHP8tvDFrPUgaKxILN1pltDk8ltnYta9opYQlnGhjXOCzlY\nypw0og/WKyuikDFy5CQ2oUuSyDJxZDFKc2BG7NxL2MmV8OxRrzK8q8YhtfUtiPNb\nawRC3B6K19T97icxRLkgBZPx0mo0+yxLO5Pvi9LgLpY/OIIZHteN02ZYedYa7JBJ\ntL06NFz4q8u+Ho79YrHg27wBNo0XiJEb5OmyaCawKJ7MPgnbjGHl1ocK1VqKE+W0\nf+J4a1unAgMBAAECggEADFNerlnd1qSMaPFAUa8G4EtR4XSp7pIFQt2/98rILqet\n66HOT2p9iD9YpSpXP1x5374JVInG2UCgIB7UfrouKRLv9uoB7BDDScohI3FuAVHC\ntPuEZ6ziBbhfgUNMSXzNp9PjLGTqO/KeXlwoAFFJ+jK3MKOfseo5UNXr9mIxykCI\nCRJbX7m+XH2FvXCsOyx6cxiRXWdlRfaK4DTQ+0Lyc/prRU/oYaHRZIp3S4+Y4uBE\nTO6T0NBdmgDgcWe38Cf2hDm7IRt00xiXMaWSsG/4DhVDNpeVqiQ3i7x/d2o3fqV7\naaneif7cNZ7id1rIWY88B1ZxtMxqTMdrNU7yC7v7KQKBgQDwtxkVO8hT0EWd5Jgj\nkFa1cAv+j5vP42axyXQQIT4l52RLYGJYiE6nym6CdTUbYUtRzz4JdzYxtMkqDoGw\nUGttJdOrRYAQIf9eJdfaBvDasbXOu3EHsVY1o3G2Gm10ubt9mciD/CiTKtBRA9Ya\nVv/VBTIOXeKAPZ23fTY9mu4ZIwKBgQDfxt+QlueUAOJPK9Fe8BxMg9Zc8eBaJWc3\n2d7eQPadBQTCP4J977Mdg3pntRpgmZhNXh/EQk7u9xWBYIQMzsaTZ4QCGnjPms7E\nwy/A23awfFqHMIDVRNrTmV5W/r8IK9s1kvaS7sUQY1RuLOHajmEZiuwFOrX2sXCl\niCpHZUGVrQKBgDosJZWqEumeZZSYz+OYWDwUzfFBB2igDgtdIf1b60cBuo00x8+Z\ncVi/ZSGF7cWmJ6unp9hlxOUSSaMuSk0vwiZog9TaQO6lKK+5+YYpMz/GvqctSU2Q\nn8LqsupNTLJuyE68QWcUI0IdkKZjhPRsnfr+/G/YZIqVWW4khl0w+eV9AoGARVvl\nxXIQex4/Bt0E+xEfJFQkqBBMQoSfVn9QBcFK7uY0UGTQ9GnMMZSj5usKLvDMdQZ8\ngB8xSf4Ji1038KRShjOqheBgm7BW8EOzVGpxgkg44vgUpoW98aHyzLIO0eCOBC/1\n/xrEt8yhybhdlJlW3Uzi1MgayEi9KoFm4VQwHM0CgYBzSa1UKioMRjDp0pWq7SB5\nYBxnMas1MOlQNguaZ9gie/zDo42ngNykir2B7moH/syluOBjq7aesD7T6K0fGrSt\n8BEg3P9/m/Iqj/nf950Q9iIlzyWSynGJkB4oc0sjNqCl+Kp6Lc6QZ6rg1avYpktT\nywajofTPeKREkKmSSRzdxQ==\n-----END PRIVATE KEY-----\n","client_email": "unos-system@persuasive-zoo-330804.iam.gserviceaccount.com","client_id": "107214931271927791902","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://oauth2.googleapis.com/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/unos-system%40persuasive-zoo-330804.iam.gserviceaccount.com"}"""

        #Start Voice Commands
        WAKE = "hey uno's"
        WAKEUP_COMMANDS = ["uno's", "who knows", "nos", "nose", "hey Uno's", "hey who knows", "hey nos", "hey nose"]
        INTRO_COMMANDS = ["hello", "hi", "",]
        EXIT_COMMANDS = ["exit", "quit", "log off", "log out", "sign out"]

        #Response Voice Command
        INTRO_RESPONSE = ["hello", "greetings", "hi", "bon jour", "ello", "hello there"]

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
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            #To use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            user_response = recognizer.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)

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