import pyttsx3 #pip install pyttsx3

sentence = input("What should I say: ") #creating input

engine = pyttsx3.init() #initialization of pyttsx3
engine.say(sentence)
engine.runAndWait() #run pyttsx3
