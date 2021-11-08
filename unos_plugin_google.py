#Modules Importer
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import pyttsx3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import os
import random
import json
from __future__ import division
import re
import sys
from google.cloud import speech
import pyaudio
from six.moves import queue


class UNOS:
    #Run the initial settings
    def __init__(self):
        self.UNOSinitialize()

    def UNOSinitialize(self):
        #Make Variables Global
        global speech
        global client
        global config
        global streaming_config
        global recognizer
        global mic
        global config
        global RATE
        global CHUNK
        global API_KEY
        global GOOGLE_CLOUD_SPEECH_CREDENTIALS
        global WAKE
        global WAKEUP_COMMANDS
        global INTRO_COMMANDS
        global EXIT_COMMANDS
        global INTRO_RESPONSE

        #Main Configurations
        config = dict(language_code="en-US")

        # Audio Recording Parameters
        RATE = 16000
        CHUNK = int(RATE / 10)  # 100ms

        #Start Voice Commands
        WAKE = "hey uno's"
        WAKEUP_COMMANDS = ["uno's", "who knows", "nos", "nose", "hey Uno's", "hey who knows", "hey nos", "hey nose"]
        INTRO_COMMANDS = ["hello", "hi", "",]
        EXIT_COMMANDS = ["exit", "quit", "log off", "log out", "sign out"]

        #Response Voice Command
        INTRO_RESPONSE = ["hello", "greetings", "hi", "bon jour", "ello", "hello there"]

        #Initilisation of Recognition Systems
        speech = pyttsx3.init()
        language_code = "en-US"  # a BCP-47 language tag

        client = speech.SpeechClient()
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code,
        )

        streaming_config = speech.StreamingRecognitionConfig(
            config=config, interim_results=True
        )

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
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            for response in responses:
            user_response = response.results[0]
 
    # def RecognizeAudio(self):
    #     #Recognition of UNOS
    #     try:
    #         user_response = recognizer.recognize(config=config, audio=mic)

    #         return str(user_response.lower())

    #     except record.UnknownValueError:
    #         return "UnknownValueError"

    #     except record.RequestError as e:
    #         return "RequestError"

    def runningCommand(self):
        #Recognition of Voice Commands
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