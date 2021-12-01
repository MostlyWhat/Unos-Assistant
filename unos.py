#Modules Importer
from __future__ import division

import json
import os
import random
import re
import sys
import time
import wave
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY

import pyaudio
import pyttsx3
import requests
import wikipedia
from audioplayer import AudioPlayer
from google.cloud import speech
from google.cloud import texttospeech
from google.cloud import texttospeech as tts
from pkg_resources import yield_lines
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from six.moves import queue

from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.logic import BestMatch, LogicAdapter
from chatterbot.response_selection import get_first_response
from chatterbot.trainers import ChatterBotCorpusTrainer


#Handles Startup and Loading Configs
class BootLoader:
    def __init__(self):
        self.BootConfig()

    def BootConfig(self):
        #Main Configurations
        global ACTIVATED
        ACTIVATED = False

        #Loading Configuration Files
        global config_file
        global database

        config_file = open('config.json')
        database = json.load(config_file)

        # Audio Recording Parameters
        global RATE
        global CHUNK
        
        RATE = 16000
        CHUNK = int(RATE / 10)  # 100ms

        #Speech to Text Configuations
        global client
        global config
        global language_code
        global streaming_config

        language_code = "en-US"
        client = speech.SpeechClient()
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code,
        )

        streaming_config = speech.StreamingRecognitionConfig(
            config=config, interim_results=True
        )

        #Deep Learning AI Configurations
        global chatbot

        chatbot = ChatBot("UNOS",
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.MathematicalEvaluation"
                },
                {
                    "import_path": "chatterbot.logic.TimeLogicAdapter"
                },
                {
                    "import_path": "chatterbot.logic.BestMatch", 
                    "statement_comparison_function": LevenshteinDistance, 
                    "response_selection_method": get_first_response,
                    'maximum_similarity_threshold': 0.5,
                    'default_response': "I'm sorry, but I don't understand the question"
                }
            ]
        )

    def BootVariables():
        #Setting Config Variables Read from Configuation Files
        global unos_name
        global unos_version
        global unos_stability
        global unos_codename
        global unos_previous_interation

        unos_name = database.get("config").get("unos_config").get("name")
        unos_version = database.get("config").get("unos_config").get("version")
        unos_stability = database.get("config").get("unos_config").get("stability")
        unos_codename = database.get("config").get("unos_config").get("codename")
        unos_previous_interation = database.get("config").get("unos_config").get("previous_interation")

        #Voice Commands
        global WAKEUP_COMMANDS
        global EXIT_COMMANDS

        WAKEUP_COMMANDS = ["hey uno's", "hey who knows", "hey nos", "hey nose"]
        EXIT_COMMANDS = ["exit", "quit", "log off", "log out", "sign out"]

    def InternetCheck(self):
        #Check Internet Connection
        url = "https://ismyinternetworking.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            return True
            
        except (requests.ConnectionError, requests.Timeout) as exception:
            return False

#Handles the Interface and Showing Status
class Interface(object):
    def setupUi(self, UNOSwindow):
        UNOSwindow.setObjectName("UNOSwindow")
        UNOSwindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(UNOSwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 801, 61))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(21)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.activateButton = QtWidgets.QPushButton(self.centralwidget)
        self.activateButton.setGeometry(QtCore.QRect(30, 350, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(22)
        self.activateButton.setFont(font)
        self.activateButton.setObjectName("activateButton")
        self.unosOutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.unosOutput.setGeometry(QtCore.QRect(300, 70, 481, 231))
        self.unosOutput.setObjectName("unosOutput")
        self.configOutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.configOutput.setGeometry(QtCore.QRect(30, 70, 251, 231))
        self.configOutput.setObjectName("configOutput")
        self.statusText = QtWidgets.QLabel(self.centralwidget)
        self.statusText.setGeometry(QtCore.QRect(30, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(14)
        self.statusText.setFont(font)
        self.statusText.setAlignment(QtCore.Qt.AlignCenter)
        self.statusText.setObjectName("statusText")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(120, 310, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(14)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.currentText = QtWidgets.QLabel(self.centralwidget)
        self.currentText.setGeometry(QtCore.QRect(300, 310, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(14)
        self.currentText.setFont(font)
        self.currentText.setAlignment(QtCore.Qt.AlignCenter)
        self.currentText.setObjectName("currentText")
        self.processLabel = QtWidgets.QLabel(self.centralwidget)
        self.processLabel.setGeometry(QtCore.QRect(520, 310, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(14)
        self.processLabel.setFont(font)
        self.processLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.processLabel.setObjectName("processLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(610, 350, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(22)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.manualInput = QtWidgets.QLineEdit(self.centralwidget)
        self.manualInput.setGeometry(QtCore.QRect(300, 350, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Industry-Book")
        font.setPointSize(22)
        self.manualInput.setFont(font)
        self.manualInput.setText("")
        self.manualInput.setObjectName("manualInput")
        UNOSwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UNOSwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.systemMenu = QtWidgets.QMenu(self.menubar)
        self.systemMenu.setObjectName("systemMenu")
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.setObjectName("helpMenu")
        UNOSwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UNOSwindow)
        self.statusbar.setObjectName("statusbar")
        UNOSwindow.setStatusBar(self.statusbar)
        self.actionAbout_UNOS = QtWidgets.QAction(UNOSwindow)
        self.actionAbout_UNOS.setObjectName("actionAbout_UNOS")
        self.preferencesButton = QtWidgets.QAction(UNOSwindow)
        self.preferencesButton.setObjectName("preferencesButton")
        self.aboutButton = QtWidgets.QAction(UNOSwindow)
        self.aboutButton.setObjectName("aboutButton")
        self.troubleshootingButton = QtWidgets.QAction(UNOSwindow)
        self.troubleshootingButton.setObjectName("troubleshootingButton")
        self.systemMenu.addAction(self.preferencesButton)
        self.helpMenu.addAction(self.aboutButton)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.troubleshootingButton)
        self.menubar.addAction(self.systemMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(UNOSwindow)
        QtCore.QMetaObject.connectSlotsByName(UNOSwindow)

    def retranslateUi(self, UNOSwindow):
        _translate = QtCore.QCoreApplication.translate
        UNOSwindow.setWindowTitle(_translate("UNOSwindow", "UNOS Assistant Launch Center"))
        self.titleLabel.setText(_translate("UNOSwindow", "UNOS Assistant Launch Center ( Version 0.0.3 )"))
        self.activateButton.setText(_translate("UNOSwindow", "ON / OFF"))
        self.statusText.setText(_translate("UNOSwindow", "STATUS: "))
        self.statusLabel.setText(_translate("UNOSwindow", "DEACTIVATED"))
        self.currentText.setText(_translate("UNOSwindow", "CURRENT PROCESS: "))
        self.processLabel.setText(_translate("UNOSwindow", "IDLE"))
        self.submitButton.setText(_translate("UNOSwindow", " SUBMIT"))
        self.systemMenu.setTitle(_translate("UNOSwindow", "System"))
        self.helpMenu.setTitle(_translate("UNOSwindow", "Help"))
        self.actionAbout_UNOS.setText(_translate("UNOSwindow", "About UNOS"))
        self.preferencesButton.setText(_translate("UNOSwindow", "Preferences"))
        self.aboutButton.setText(_translate("UNOSwindow", "About UNOS"))
        self.troubleshootingButton.setText(_translate("UNOSwindow", "Troubleshooting"))


#Handles Voice Recognition to Running Commands
class UNOS:


#Getting the MicrophoneStream Data (Source: Google Cloud)
class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)