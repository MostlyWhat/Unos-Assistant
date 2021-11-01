#Modules Importer
import speech_recognition as record
import pyttsx3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import unos

unos.UNOSinitialize()
unos.Verify()
unos.StartupText()
#unos.MainWindow()

while True:
    response = unos.RecognizeUNOS()

    if response == "Continue":
        #DO

    else:
        print(response)