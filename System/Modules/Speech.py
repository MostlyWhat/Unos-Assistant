import json
import queue
import sys
import pyaudio
import pyttsx3
import requests
import sounddevice as sd
import vosk
from google.cloud import speech
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

config = Config()
crisis = Crisis()

#Main Configurations
language_code = 'en-US'
WAKEUP_COMMANDS = config.wakeup_commands
RATE = 16000
CHUNK = RATE // 10

# Vosk Configurations
if config.voice_recognition is True and config.providers_recognition == "vosk":
    q = queue.Queue()
    model = vosk.Model(lang="en-us")

# Google Audio Recording Parameters
if config.providers_recognition == "google" or config.providers_text_to_speech == "google":
    client = speech.SpeechClient()
    config_speech = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config_speech, interim_results=True
    )

class Speaker():
    def __init__(self):
        # init function to get an engine instance for the speech synthesis
        # if config.providers_text_to_speech == "pyttsx3":
        #     self.engine = pyttsx3.init()

        # else:
        #     self.engine = pyttsx3.init()
        self.engine = pyttsx3.init()

    def speak(self, text):
        # if config.providers_text_to_speech == "pyttsx3":
        #     # say method on the engine that passing input text to be spoken
        #     self.engine.say(text)

        #     # run and wait method, it processes the voice commands.
        #     self.engine.runAndWait()

        # else:
        #     # say method on the engine that passing input text to be spoken
        #     self.engine.say(text)

        #     # run and wait method, it processes the voice commands.
        #     self.engine.runAndWait()

        # say method on the engine that passing input text to be spoken
        self.engine.say(text)

        # run and wait method, it processes the voice commands.
        self.engine.runAndWait()

class Listener():  # Listener class to get the input from the user
    def __init__(self):
        # init function to get an engine instance for the speech synthesis
        pass

    def listenForUNOS(self):
        #Recognition of Audio requests
        while True:
            wakeup = self.RecognizeUNOS()

            if wakeup is True:
                return True

            else:
                crisis.log("Speech", "Wakeup Failed")

    def listenForCommand(self):
        return self.RecognizeAudio()

    def RecognizeUNOS(self):
        # Recognition of UNOS requests        
        if config.providers_recognition == "google":
            user_response = GoogleRecognizer.RecognizeAudio(self)

        else:
            user_response = VoskRecognizer.RecognizeAudio(self)

        if user_response in WAKEUP_COMMANDS:
            return True

    def RecognizeAudio(self):
        #Recognition of Audio requests
        if config.providers_recognition == "google":
            user_response = GoogleRecognizer.RecognizeAudio(self)

        else:
            user_response = VoskRecognizer.RecognizeAudio(self)

        return user_response

# Real-time Audio Stream to get the audio input from the user
class VoskRecognizer:
    @staticmethod
    def RecognizeAudio():
        #Recognition of Audio requests
        with sd.RawInputStream(samplerate=RATE, blocksize = 8000, dtype='int16', channels=1, callback=VoskRecognizer.callback):
            rec = vosk.KaldiRecognizer(model, RATE)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    return result["text"]

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

class GoogleRecognizer:
    @staticmethod
    def RecognizeAudio():
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
                    if result.is_final:
                        transcript = (result.alternatives[0].transcript)
                        overwrite_chars = " " * (num_chars_printed - len(transcript))

                        user_response = (transcript + overwrite_chars)
                        return str(user_response.lower())

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
