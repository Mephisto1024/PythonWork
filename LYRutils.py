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
        img_name = 'test_1.png'
        f = open(img_name, 'rb')
        # 转 base64
        img_base64 = base64.b64encode(f.read())
        
        return img_base64
        
        
        
    def gethtml(self,img_base64):
        
        beautify_url = "https://api-cn.faceplusplus.com/facepp/v2/beautify"
        # 你创建的应用的 API Key 和 API Secret(也叫 Secret Key)
        AK = 'ymsWTOvoWbh1UJ9z9WNs2tF_XxlvsWtS'
        SK = 'JgSoZxCLllFdRFETv9zHLvtkmHjOr2A8'
        
        # 可选参数，不填写，默认50
        # 美白程度 0 - 100
        whitening = 80
        # 磨皮程度 0 - 100
        smoothing = 80
        # 瘦脸程度 0 - 100
        thinface = 100
        # 小脸程度 0 - 100
        shrink_face = 50
        # 大眼程度 0 - 100
        enlarge_eye = 50
        # 去眉毛程度 0 - 100
        remove_eyebrow = 50
        # 滤镜名称，不填写，默认无滤镜
        filter_type = ''
        
        # 使用 whitening、smoothing、thinface 三个可选参数，其他用默认值
        data = {
            'api_key': AK,
            'api_secret': SK,
            'image_base64': img_base64,
            'whitening': whitening,
            'smoothing': smoothing,
            'thinface': thinface,
            }
 
        r = requests.post(url=beautify_url, data=data)
        html = json.loads(r.text)
        
        return html
        
        
        
    def analysisbase64(self,html):
        # 解析base64图片
        base64_data = html['result']
        imgData = base64.b64decode(base64_data)
        nparr = np.frombuffer(imgData, np.uint8)
        img_res = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img_res_BGR = cv2.cvtColor(img_res, cv2.COLOR_RGB2BGR)
        
        return img_res_BGR
        
        
        
    def Originalimg(self,img_name):
        # 原始图片
        img = cv2.imread(img_name)
        img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        return img_BGR
    
            
    
    






