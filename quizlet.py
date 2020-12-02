import requests
from gtts import gTTS
import os

txt = '''flower	お花
waterfall	滝
car	車'''

newText = txt.split("\n")
d = {}

for i in newText:

  keyVal = i.split("\t")
  d[keyVal[0]] = keyVal[1]

print(d)

'''
language = 'ja'

myObj = gTTS(text = txt, lang = language, slow=False)

myObj.save("txt.mp3")
'''
with open('text.mp3','wb') as fp:
	for i in d:
		eng = gTTS(i,lang='en')
		jap =  gTTS(d[i], lang='ja')
		eng.write_to_fp(fp)
		jap.write_to_fp(fp)
