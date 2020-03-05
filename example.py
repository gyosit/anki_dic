import math
import os
import re
import requests
import shutil
from bs4 import BeautifulSoup
from googletrans import Translator
from google_images_download import google_images_download
import csv
import pprint
import json
import pyttsx3
from gtts import gTTS
import time

translator = Translator()
response = google_images_download.googleimagesdownload()

def rmEx(text):
  text = re.sub(' \[.*\]', '', text)
  text = re.sub(' \(.*\)', '', text)
  text = re.sub('\[.*\]', '', text)
  text = re.sub('\(.*\)', '', text)
  text = re.sub('《.*》', '', text)
  return text

def downloadPic(word, keyword):
  keyword = re.sub('\.', '', keyword)
  keyword = re.sub('\,', '', keyword)
  keyword = re.sub('\?', '', keyword)
  keyword = re.sub('\!', '', keyword)
  arguments = {"keywords":word, "limit":1, "print_urls":True}
  paths = response.download(arguments)
  paths = paths[0][word][0]
  
  os.rename(paths, "./images/" + word + ".jpg")

def createVoice(word, text, lang):
  tts = gTTS(text=text, lang=lang)
  tts.save("./sound/" + word + "_" + lang + ".mp3")

def weblio(word):
  r = requests.get("https://ejje.weblio.jp/content/" + word)
    
  soup = BeautifulSoup(r.content, "html.parser")

  enlist = soup.find_all("span", "KejjeYrEn")
  jplist = soup.find_all("span", "KejjeYrJp")

  enl = len(enlist)

  if(enl==0):
    en = word
    jplist = soup.find_all("td", "conatent-explanation ej")
    jpl = len(jplist)
    if(jpl==0):
      jp = "YABEE"
      return en, jp
    jp = jplist[0].text
    if('ミススペル' in jp):
      en = jp[0:jp.find('（')]
      en, jp = weblio(en)
      #jp = re.search(r'(?<=（).*?(?=\）)', jp)[0]
    return en, jp
  else:
    en = rmEx(enlist[0].text)
    jp = rmEx(jplist[0].text)

  return en, jp

def translate():
  full_data = []

  with open('./english2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      origin = row[0]

      en, jp = weblio(origin)
      print(en, jp)
      full_data = [[origin, en, jp]]
      time.sleep(1)

      with open('./new_test.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(full_data)

def addVoice():
  # 音声を作成＋新しいcsvの作成
  lang = "nl"

  full_data = []

  with open('input/Dutch20200229.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      word = row[0]
      text = row[1]
      jp_text = row[2]
      print(word, text, jp_text)

      createVoice(word, text, lang)

      full_data.append([text+' [sound:' + word + '_' + lang + '.mp3]', jp_text])
    
  with open('./output.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(full_data)

#translate()
addVoice()