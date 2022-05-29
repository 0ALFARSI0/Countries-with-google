import re
from gtts import gTTS

f = open('countries.txt','r')
countries = re.split("\n",f.read())

for i in countries:
 tts = gTTS(f"{i}")
 tts.save(f"{i}.mp3")