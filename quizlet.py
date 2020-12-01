import requests
import cloudscraper
txt = '''flower	お花
waterfall	滝
car	車'''

newText = txt.split("\n")
d = {}

for i in newText:

  keyVal = i.split("\t")
  d[keyVal[0]] = keyVal[1]

#print(d)

url = "https://quizlet.com/551833561/edit"

scraper = cloudscraper.create_scraper()

print(scraper.get(url).text)
