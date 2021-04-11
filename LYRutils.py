# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:05:40 2021

@author: 27452
"""

import requests
import base64
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk



class beautify():
    
    def openimg(self):
        img_name = 'test_2.png'
        f = open(img_name, 'rb')
        # change into base64
        img_base64 = base64.b64encode(f.read())
        
        return img_base64
        
        
        
    def gethtml(self,img_base64):
        
        beautify_url = "https://api-cn.faceplusplus.com/facepp/v2/beautify"
        # API key and API secret (also called secret key) of the application you create
        AK = 'ymsWTOvoWbh1UJ9z9WNs2tF_XxlvsWtS'
        SK = 'JgSoZxCLllFdRFETv9zHLvtkmHjOr2A8'
        
        # Optional parameter. If it is not filled in, the default value is 50
        # Whitening degree 0 - 100
        whitening = 80
        # Degree of skin grinding 0 - 100
        smoothing = 80
        # The degree of thin face 0 - 100
        thinface = 100
        # Degree of small face 0 - 100
        shrink_face = 50
        # Macrophthalmia degree 0 - 100
        enlarge_eye = 50
        # Degree of eyebrow removal 0 - 100
        remove_eyebrow = 50
        # Filter name. If it is not filled in, there is no filter by default
        filter_type = ''
        
        # use whitening、smoothing、thinface three optional parameters, others with default values
        data = {
            'api_key': AK,
            'api_secret': SK,
            'image_base64': img_base64,
            'whitening': whitening,
            'smoothing': smoothing,
            'thinface': thinface,
            'shrink_face':shrink_face,
            'enlarge_eye':enlarge_eye,
            'remove_eyebrow':remove_eyebrow,
            'filter_type':filter_type,
            }
 
        r = requests.post(url=beautify_url, data=data)
        html = json.loads(r.text)
        
        return html
        
        
        
    def analysisbase64(self,html):
        # Analysis of Base64 pictures
        base64_data = html['result']
        imgData = base64.b64decode(base64_data)
        nparr = np.frombuffer(imgData, np.uint8)
        img_res = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img_res_BGR = cv2.cvtColor(img_res, cv2.COLOR_RGB2BGR)
        
        return img_res_BGR
        
        
        
    def Originalimg(self,img_name):
        # Original picture
        img = cv2.imread(img_name)
        img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        return img_BGR

    def showimg(self,img_BGR,img_res_BGR):
        fig, axs = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(10,10))
        axs[0].imshow(img_BGR)
        axs[1].imshow(img_res_BGR)
        plt.show()


