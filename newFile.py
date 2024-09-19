import pyttsx3
import sys
# Read the Russian word from the text file

with open('russian_word.txt', 'r', encoding='utf-8') as file:
    text = file.read()

engine = pyttsx3.init()
# Rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)
#voice
engine.say(text)
    
engine.runAndWait()

sys.exit()
