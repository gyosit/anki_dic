import csv
import pprint
import requests
import json
import pyttsx3
from gtts import gTTS

engine = pyttsx3.init()

preurl = 'https://wordsapiv1.p.mashape.com/words/'
method = '/examples'
params = {
  "X-Mashape-Key":"86c3bc611emsh19c905635bd62a6p105f4fjsn52fe84814712",
  "Accept":"application/json"
}
s_org = ' [sound:REPLACE.mp3]'
S_ORG = ' [sound:REPLACE.mp3]'

full_data = []

MODE = 1 # 1:Word 2:Sentence

with open('input/dutch2.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    if(MODE==1):
      eng = row[0]
      lang = row[1]
      print(eng, lang)

      #音声
      tts = gTTS(text=lang, lang='nl')
      tts.save("./sound/" + lang + "_word.mp3")

      #結合
      newlang = lang + s_org.replace("REPLACE", lang+"_word")
      full_data.append([eng, newlang])

    elif(MODE==2):
      eng = row[0]
      jp = row[1]
      print(eng)

      sentence = ""
      """
      #辞書
      url = preurl + eng + method
      #print(url)
      res = requests.get(url, headers=params)
      json_dict = res.json()
      blank = ""
      #print(json_dict)
      if('examples' in json_dict and len(json_dict['examples'])>0):
        sentence = json_dict['examples'][0]
        blank = sentence.replace(eng, '__')
      else:
        sentence = ""
        blank = ""
      """

      #音声
      tts = gTTS(text=eng, lang='nl')
      tts.save("./sound/" + eng + "_word.mp3")

      #結合
      neweng = eng + s_org.replace("REPLACE", eng+"_word")
      if(sentence==""):
        newjp = jp
      else:
        newjp = jp + "<br>" + blank
      full_data.append([neweng, newjp])
  
with open('output/newanki.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerows(full_data)