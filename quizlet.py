import requests
from gtts import gTTS
import os

txt = '''flower	お花
waterfall	滝
car	車'''

def quizletmp3(text):
	newText = text.split("\n")
	d = {}

	for i in newText:

	  keyVal = i.split("\t")
	  d[keyVal[0]] = keyVal[1]

	print(d)

	with open('text.mp3','wb') as fp:
		for i in d:
			eng = gTTS(i,lang='en',slow=False)
			jap =  gTTS(d[i], lang='ja',slow=True)

			eng.write_to_fp(fp)
			gTTS("3, 2, 1", lang = 'en', slow=False).write_to_fp(fp)
			jap.write_to_fp(fp)

quizletmp3(txt)
