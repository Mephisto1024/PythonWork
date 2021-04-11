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


img_name = 'test_1.png'

img_base64 = bea.openimg()
html = bea.gethtml(img_base64)
img_res_BGR = bea.analysisbase64(html)
img_BGR = bea.Originalimg(img_name)


# 显示图片
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(10,10))
axs[0].imshow(img_BGR)
axs[1].imshow(img_res_BGR)
plt.show()



