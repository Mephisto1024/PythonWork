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
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk


from LYRutils import beautify
from LYRutils import tkinter_


bea = beautify()
tki = tkinter_()



window = tk.Tk()
window.title("beautify owo~")
window.geometry('650x450+150+100')

img_name = 'test_1.png'
img_base64 = bea.openimg()
html = bea.gethtml(img_base64)
img_res_BGR = bea.analysisbase64(html)
img_BGR = bea.Originalimg(img_name)

        
b1 = tk.Button(window,text="show original image",width=15,height=2,command=tki.show(window,img_BGR))
b1.pack()
        
b2 = tk.Button(window,text="show beautiful image",width=15,height=2,command=tki.showres(window,img_res_BGR))
b2.pack()
        
window.mainloop()





# 显示图片
#fig, axs = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(10,10))
#axs[0].imshow(img_BGR)
#axs[1].imshow(img_res_BGR)
#plt.show()



