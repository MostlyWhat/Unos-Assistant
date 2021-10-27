import speech_recognition as record
import pyttsx3
import sys

recognizer = record.Recognizer()
mic = record.Microphone()

with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print(recognizer.recognize_google(audio))
except record.UnknownValueError:
    print("UNOS: ERROR RECOGNISING THE SPEECH, PLEASE TRY AGAIN")
except record.RequestError as e:
    print("UNOS: ERROR REQUESTING TO GOOGLE API SERVERS; {0}".format(e))