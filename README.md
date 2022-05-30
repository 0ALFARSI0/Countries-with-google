# Countries-with-google
 Nothing emprissive here just a normal code that generate countries names with mp3
<hr>
If you're wondering how this code work , let me tell you

```py
import re
from gtts import gTTS 
```
First thing i import the libraries,<br>
gtts, to translate the text to an audio<br>
re  , to open the text file and read it...

```py
f = re.open("countries.txt","r")
```
Then i defined a variable that open the file as a reader

```py
Countries = re.split("\n",f.read())
```
Then, i defined a variable that open the file and read it, then split it in every line break(\n) and make it in a list

```py
for i in Countries:
 tts = gTTS(f"{i}")
 tts.save(f"{i}.mp3")
```
So, here, i defined a for loop , to run in the list, in every index , it stop and get the index and defined it to the (i), so i made a new object that have this variable as a text , then i save the audio file as MP3.
<hr>

```py

import re
from gtts import gTTS

f = open('countries.txt','r')
countries = re.split("\n",f.read())

for i in countries:
 tts = gTTS(f"{i}")
 tts.save(f"{i}.mp3")
```
