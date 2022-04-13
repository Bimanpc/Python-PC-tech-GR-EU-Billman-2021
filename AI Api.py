import speech_recognition as sr
recording = sr.Recognizer()
with sr.Microphone() as source: recording.adjust_for_ambient_noise(source)
   print("Please Say .....:")
   audio = recording.listen(source)
   