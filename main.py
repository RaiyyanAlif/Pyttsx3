import pyttsx3

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()
  
  
speak("Hey you whats up guys its mr. triple r and welcome to my channel niye aslam tumader jonno aro ekta special video")
