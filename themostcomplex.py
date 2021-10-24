import pyttsx3

while True:
  sentence = input()
  engine = pyttsx3.init()
  engine.say(sentence)
  engine.runAndWait()
