# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:05:26 2021

@author: 27452
"""

import requests
import base64
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt


from LYRutils import beautify


bea = beautify()


img_name = 'test_2.png'

img_base64 = bea.openimg()
html = bea.gethtml(img_base64)
img_res_BGR = bea.analysisbase64(html)
img_BGR = bea.Originalimg(img_name)

bea.showimg(img_BGR,img_res_BGR)

