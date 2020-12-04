import requests
from gtts import gTTS
import os

txt = '''good	いい
early	はやい
new	あたらしい
hot weather	あつい
busy	いそがしい
large	おおきい
interesting	おもしろい
frightening	こわい
cold weather	さむい
fun	たのしい
small	ちいさい
boring	つまらない
old	ふるい
difficult	むずかしい
easy	やさしい
cheap	やすい
expensive	たかい
dislike	きらいな
clean	きれいな
healthy	げんきな
quiet	しずかな
fond of	すきな
to hate	だいきらいな
to love	だいすきな
lively	にぎやかな
handsome	ハンサムな
not busy	ひまな
tough	たいへんな
smart	あたまがいい
great looking	かっこいい
cute	かわいい
tall	せがたかい
short stature	せがひくい
long	ながい
fast	はやい
short length	みじかい
kind	しんせつな
convenient	べんりな
skillful	じょうずな
clumsy	へたな
famous	ゆうめいな'''

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
		eng = gTTS(i,lang='en',slow=True)
		jap =  gTTS(d[i], lang='ja',slow=True)
		eng.write_to_fp(fp)
		gTTS("3, 2, 1", lang = 'en', slow=True).write_to_fp(fp)
		jap.write_to_fp(fp)
