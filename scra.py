__author__ = 'Simon'

from io import BytesIO
import os
import PIL, requests
import numpy as np
from PIL import Image
import re

# Import html from URL

URL =  "https://www.tensorflow.org/"
response = requests.get(URL)
html = response.text

# looking for this <img src="https://www.xxxxxxx.com/.../transparent.png"
# search for <img src=" ... " using regex pattern
pattern = re.compile("<img src=\"[^\"]*\"")
match_text = pattern.finditer(html)
# slice away tags and quotationmark of the found match objects
img_urls = [item.group()[10:-1] for item in match_text]
print( "Found %i images on page "%len(img_urls)+URL)

# TESTIMAGE -------
# test_request_response = requests.get(img_urls[0])
# Testimage = Image.open(BytesIO(test_request_response.content))
# Image.Image.show(Testimage)

#creating new directory if not existing
mypath = os.path.dirname(os.path.abspath(__file__))
print(mypath)
#include url into dir name
newdir = mypath + "\\"+URL[-15:]
print(newdir)
#check if dir already exists if not create it
if not os.path.isdir(newdir):
   print("Creating new dir at "+newdir)
   os.makedirs(newdir)

#saving images to newdir filepath
for i in range(len(img_urls)):

   try:

      request_response = requests.get(img_urls[i])

      res_img = Image.open(BytesIO(request_response.content))

      filepath = newdir+"\\"
      filename = filepath + str(i) + ".jpg"
      res_img.save(filename)
   except:
      #print imgsrc that cannot be opened
      print("could not open: ")
      print(img_urls[i])
      print(i)
