import re
import requests
from bs4 import BeautifulSoup
import csv
import time
import sys

def rmEx(text):
  text = re.sub(' \[.*\]', '', text)
  text = re.sub(' \(.*\)', '', text)
  text = re.sub('\[.*\]', '', text)
  text = re.sub('\(.*\)', '', text)
  text = re.sub('《.*》', '', text)
  return text

def weblio(word):
  r = requests.get("https://ejje.weblio.jp/content/" + word)
    
  soup = BeautifulSoup(r.content, "html.parser")

  jp_word = soup.find_all("td", class_="content-explanation ej") # 日本語訳
  enlist = soup.find_all("span", "KejjeYrEn") # 英文
  jplist = soup.find_all("span", "KejjeYrJp") # 英文和訳

  enl = len(enlist)

  if(enl==0):
    # 英文がない場合
    if('ミススペル' in jp_word):
      # ミススペル候補が出てきた場合(元々の英単語がタイポ)
      new_word = jp[0:jp.find('（')]
      en, jp = weblio(new_word) # 再検索
      #jp = re.search(r'(?<=（).*?(?=\）)', jp)[0]
      return en, jp

    new_word = soup.find_all("div", "nrCntSgT")
    if(len(new_word)!=0):
      # 他の単語候補がある場合
      en, jp = weblio(new_word)
      return en, jp

    if(jp_word==[]):
      jp_word = ""
    else:
      jp_word = jp_word[0].text
    en_sent = ""
    jp_sent = ""
  else:
    # 正しく検索できた場合
    jp_word = jp_word[0].text
    en_sent = enlist[0].text
    jp_sent = jplist[0].text

  #print(word, en_sent, jp_word, jp_sent)

  en = word + "<br>" + en_sent
  jp = jp_word + "<br>" + jp_sent

  return en, jp

def translate(filename):
  full_data = []

  with open("input/"+filename) as f:
    reader = csv.reader(f)
    for row in reader:
      origin = row[0]

      en, jp = weblio(origin)
      print(en, jp)
      full_data = [[origin, jp, en]]
      time.sleep(1)

      with open("output/"+filename, 'a', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(full_data)

if __name__ == "__main__":
  args = sys.argv
  if(len(args)>1):
    translate(args[1])
  else:
    print("Enter File name: ./example.exe <file name>")