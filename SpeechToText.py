#pip install SpeechRecognition

import speech_recognition as sr
r = sr.Recognizer()

soundfile=sr.AudioFile('short_test.wav') #the local file
with soundfile as source:
    audio = r.record(source)
try:
    soundfile_text = r.recognize_google(audio)
    print("Text: "+soundfile_text)
except Exception as e:
    print("Exception: "+str(e))
    
with open('soundfile_text.txt', 'w') as f: #, encoding="utf-8") for Bulgarian
    print(soundfile_text, file=f)

