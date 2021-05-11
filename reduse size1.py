# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:13:16 2021

@author: sarth
"""

from PIL import Image
import PIL
import os
import glob

file_name = 'test123.jpg'
picture = Image.open('t.jpg')
dim = picture.size
picture.save(file_name,quality=10) 