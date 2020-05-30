# Install speech_recognition with pip install speech_recognition
# Install pyaudio with pip install pyaudio
# Make sure you look up full instructions for installing pyaudio

import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)

output = recognizer.recognize_google(audio)

print(output)
