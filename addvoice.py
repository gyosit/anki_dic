import csv
from gtts import gTTS
import sys

def createVoice(word, text, lang):
  tts = gTTS(text=text, lang=lang)
  if(lang == "en-gb"):
    lang ="en"
  tts.save("./sound/" + word + "_" + lang + ".mp3")

def addVoice(filename, lang="en-gb"):
  # 音声を作成＋新しいcsvの作成
  full_data = []

  with open('input/'+filename) as f:
    reader = csv.reader(f)
    for row in reader:
      word = row[0] # 単語
      text = row[2] # 現地語
      word_ = word.replace("/", "")
      text_ = text.replace(".", "")
      jp_text = row[1] # 日本語
      print(word, text, jp_text)

      #createVoice(word, text_, lang)
      createVoice(word_, word, lang)

      full_data = [["["+lang+"]"+jp_text, text+' [sound:' + word_ + '_' + lang + '.mp3]']]
    
      with open('output/'+filename, 'a', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(full_data)

if __name__ == "__main__":
  args = sys.argv
  if(len(args)>2):
    addVoice(args[1], args[2])
  else:
    print("Enter File name and language code: ./addvoice.exe <file name> <language code>")