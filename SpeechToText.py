'''
#pip install SpeechRecognition
'''
# 1. Imports & Sample Files

import speech_recognition as sr
r = sr.Recognizer()
sound_file1 = "https://raw.githubusercontent.com/tvelichkovt/SpeechToText/master/Sample_Files/SpeechToText_Sample.wav"
soundfile=sr.AudioFile(sound_file1) #the local file

with soundfile as source:
    audio = r.record(source)
try:
    soundfile_text = r.recognize_google(audio)
    print("Text: "+soundfile_text)
except Exception as e:
    print("Exception: "+str(e))
    
with open('SpeechToText_Output.txt', 'w') as f: #, encoding="utf-8") for Bulgarian
    print(soundfile_text, file=f)

