# anki_dic
Create Anki deck from weblio and make audios

example.pyを使用

## 使い方(Weblioスクレイピング)
*単語リストから例文一覧を作成する
1. csvを作成

|A|
|:--|
|apple|
|banana|
|cabbage|
2. translate()内の`with open('./***.csv') as f:`を1.のファイル名に変更
3. translate()の出力するファイル名`with open('./***.csv', 'a') as f:`を変更
4. translate()を実行
5. 例文入り単語帳が生成

|A|B|C|
|:--|:--|:--|
|apple|I eat an apple.|私はりんごを食べる。|
|banana|Bananas are yellow.|バナナは黄色い。|
|cabbage|Do you like cabbages?|キャベツは好きですか?|

## 使い方(音声作成)
* example.pyと同じ階層にsound/ディレクトリを作成しておく。
1. csvを作成(translate関数から作成可能)

|A|B|C|
|:--|:--|:--|
|apple|I eat an apple.|私はりんごを食べる。|
|banana|Bananas are yellow.|バナナは黄色い。|
|cabbage|Do you like cabbages?|キャベツは好きですか?|
2. addVoice()の`with open('***.csv') as f:`を1.のファイル名に変更
3. langをB列の言語に変更(言語コードはおそらくhttps://cloud.google.com/speech-to-text/docs/languages　と同じ)
4. addVoice()の出力ファイル名`with open('./***.csv', 'w') as f:`を変更
5. addVoice()を実行
6. sound/に音声ファイルが生成
7. Anki対応音声情報付きcsvファイルが生成

|A|B|
|:--|:--|
|I eat an apple. [sound:apple_en.mp3]|私はりんごを食べる。|
|Bananas are yellow. [sound:banana_en.mp3]|バナナは黄色い。|
|Do you like cabbages? [sound:cabbage_en.mp3]|キャベツは好きですか?|

## 応用例
*英語以外の言語デッキを作成する場合は、音声作成時のcsvファイルB, C列を自分で作成するか、Google Spread SheetのGOOGLETRANSLATE関数で翻訳します。
