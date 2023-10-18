# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:41:04 2023

@author: Alp GEDIKLI
"""

from PIL import Image
import pytesseract

img = Image.open("ex2.jpg")

text = pytesseract.image_to_string(img,lang="eng")
print(text)

##resmi gray yap
##resmi gray uzerinden yumusatalim -- bilateralFilter
##sonrasinda cannyedge ile koseleri algiliyoruz
##kontorleri buluyourz
##imutils.grab ile konturler yakalinir
##degerler siralanir sort ile 