#Modules Importer
from __future__ import division
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from pkg_resources import yield_lines
import pyttsx3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time
import os
import random
import json
import re
import sys
from google.cloud import speech
from google.cloud import texttospeech as tts
import pyaudio
from six.moves import queue
import re
import wave
from audioplayer import AudioPlayer
from google.cloud import texttospeech
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.logic import BestMatch
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.logic import LogicAdapter
import wikipedia
import requests

class BootLoader:
    #Verification Before Launch
    def Verify(self):
        continue_flag = input("Warning! UNOS is unstable in it's current state. Are you sure you want to continue? (y/N): ")

        if continue_flag == "y":
            print("BootLoader: Launching UNOS")
            time.sleep(3)
            return True

        else:
            print("BootLoader: Startup Failed")
            time.sleep(3)
            return False

    #Startup Text
    def StartupText(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        boot_sequence = open("boot_sequence.txt")
        boot_text = boot_sequence.readlines()
        for line in boot_text:
            print(line, end="")
            time.sleep(random.uniform(0,0.10))
        
        print(" ")
        print("BootLoader: Boot Complete")
        print(" ")
        time.sleep(5)

        os.system('cls' if os.name == 'nt' else 'clear')

        print(" ")                               
        print("[ UNIFIED NON-INTELLIGENT-ASSISTANT OPEN-SOURCED SYSTEM ]")
        print(" ")    
        print("Developed by MostlyWhat under S.K.Y.N.E.T Assistant Program")
        print(" ")
        print("Name: U.N.O.S") #Put in Variables Please!
        print("Version: 0.0.2-beta") #Put in Variables Please!
        print("Codename: Megatron") #Put in Variables Please!
        print("Status: Partially Stable") #Put in Variables Please!
        print("Previous Interation: SKYNET v0.0.1-alpha") #Put in Variables Please!
        print(" ")    
        print("UNOS: System Ready for Inquiry")
        AudioPlayer("audio/Systems_Ready.mp3").play(block=True)

    def InternetCheck(self):
        #Check Internet Connection
        url = "https://ismyinternetworking.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            print("BootLoader: Connected to the Internet")
            time.sleep(3)
            return True
            
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("BootLoader: No Internet Connection.")
            return False

class UNOS:
    """UNOS's main class that handles everything from booting to executing commands."""
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
        global pspeech
        global voice_name
        global RATE
        global CHUNK
        global API_KEY
        global GOOGLE_CLOUD_SPEECH_CREDENTIALS
        global WAKE
        global WAKEUP_COMMANDS
        global INTRO_COMMANDS
        global EXIT_COMMANDS
        global INTRO_RESPONSE
        global chatbot

        #Main Configurations
        config = dict(language_code="en-US")

        # Audio Recording Parameters
        RATE = 16000
        CHUNK = int(RATE / 10)  # 100ms

        #Start Voice Commands
        WAKE = "hey who knows"
        WAKEUP_COMMANDS = ["uno's", "who knows", "nos", "nose", "hey uno's", "hey who knows", "hey nos", "hey nose"]
        INTRO_COMMANDS = ["hello", "hi", "bon jour",]
        EXIT_COMMANDS = ["exit", "quit", "log off", "log out", "sign out"]

        #Response Voice Command
        INTRO_RESPONSE = ["hello", "greetings", "hi", "bon jour", "ello", "hello there"]

        #Initilisation of Recognition Systems
        pspeech = pyttsx3.init()
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

        #Initilisation of ChatBot
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

    #Saying Speech
    def speak(self, audio: str):
        if audio == "E":
            AudioPlayer("output.mp3").play(block=True)
            return None
            
        elif audio == "Ready_Inquiry":
            AudioPlayer("audio/Ready_Inquiry.mp3").play(block=True)
            return None

        #Generate Audio if not Specified by Pre-Recorded Audio
        else:
            self.create_audio_tts(audio)
            AudioPlayer("audio/output.mp3").play(block=True)

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

    def create_audio_tts(self, text):
        """Synthesizes speech from the input string of text."""
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.SynthesisInput(text=text)
        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )
        audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )
        # The response's audio_content is binary.
        with open("audio/output.mp3", "wb") as out:
            out.write(response.audio_content)

    def RecognizeUNOS(self):
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            num_chars_printed = 0

            # Now, put the transcription responses to use.
            for response in responses:
                # Once the transcription has settled, the first result will contain the
                # is_final result. The other results will be for subsequent portions of
                # the audio.
                for result in response.results:
                    transcript = (result.alternatives[0].transcript)
                    overwrite_chars = " " * (num_chars_printed - len(transcript))

                    if result.is_final:
                        user_response = (transcript + overwrite_chars)

                        if user_response in WAKEUP_COMMANDS:
                            return True

                        else:
                            return str(user_response.lower())
        
    def RecognizeAudio(self):
        #Recognition of Audio requests
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            num_chars_printed = 0

            # Now, put the transcription responses to use.
            for response in responses:
                # Once the transcription has settled, the first result will contain the
                # is_final result. The other results will be for subsequent portions of
                # the audio.
                for result in response.results:
                    transcript = (result.alternatives[0].transcript)
                    overwrite_chars = " " * (num_chars_printed - len(transcript))

                    if result.is_final:
                        user_response = (transcript + overwrite_chars)
                        return str(user_response.lower())

    def runningCommand(self):
        #Recognition of Voice Commands
        self.speak("Ready_Inquiry")
        print("UNOS: Command Input")
        command = (self.RecognizeAudio()).lower()
        print("UNOS: Command Detected ( " + command + " )")

        # for exit_commands in EXIT_COMMANDS:
        #     exit_check = bool(re.match(r"\b(exit|quit|end|log out)\b", command, re.I))
        #     if exit_check == True:
        #         print("UNOS: Shutting Down System")
        #         self.speak("shutting down system")
        #         exit()

        if command in EXIT_COMMANDS:
            print("UNOS: Shutting Down System")
            self.speak("shutting down system")
            exit()

        elif "search" in command:
            try:
                #remove the word "search" and use wikipedia to search
                search_subject = command.replace("search", "")
                searched_data = wikipedia.summary(search_subject, sentences=2)
                print("UNOS: Data Collected")
                print(searched_data)
                self.speak(searched_data)

            except wikipedia.exceptions.WikipediaException:
                print("UNOS: Article Not Found or Unable to Connect to Wikipedia API")
                self.speak("article not found or unable to connect to wikipedia API")

            finally:
                print("UNOS: Command Finished")

        else:
            response = str(chatbot.get_response(command))
            print("UNOS: " + response)
            self.speak(response)
            print("UNOS: Command Finished")

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