#Modules Importer
import speech_recognition as record
import pyttsx3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
from unos_plugin import UNOS

unos = UNOS()
unos.UNOSinitialize()
verification = unos.Verify()

def main():
    while True:
        activated = unos.RecognizeUNOS()

        if activated == "True":
            
            command = unos.RecognizeCommand()


        else:
            print("no")

if verification == "True":
    unos.StartupText()
    main()
    #unos.MainWindow()

else:
    exit()