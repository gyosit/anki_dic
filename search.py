import os
import shutil

def searchPic(path, topath):
  for pathname, dirnames, filenames in os.walk(path):
    for filename in filenames:
      fullpass = os.path.join(pathname, filename)
      print(fullpass)
      shutil.move(fullpass, topath+"/"+filename)

searchPic("./downloads", "./images")