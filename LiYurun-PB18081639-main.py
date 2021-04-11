# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:52:46 2021

@author: 27452
"""
import os
from urllib import parse
import requests
from docx import Document
from lxml import etree
import re
import random
from multiprocessing import Pool

import time


from LiYurunPB18081639utils import biqugeCrawl
   
if __name__ == '__main__':
    biquge = biqugeCrawl()
    print("----Biquge Book Crawler----")
    print("1-------------search book")
    print("2--------------------exit")

    flag = input("Please input the command to select the corresponding function：")

    while 1:
        error_str = ""

        if flag == "1":
            book = biquge.search_book()
  
            if book is not None:
                flag = input("The name of the book is《{}》，the author's name is{},please confirm whether to download【Y/N】".format(book[0], book[1]))
                while 1:
                    if flag == 'Y' or flag == 'y':
                        biquge.download(book[0], book[2])
                        break
                    elif flag == 'N' or flag == 'n':
                        break
                    else:
                        flag = input("Please input correctly【Y/N】!")
            else:
                print("There is no such book QAQ")

        elif flag == "2":
            exit(1)

        else:
            error_str = "Instruction error，"
        flag = input("{}please re-enter the command to select the corresponding function【1.search；2.exit】：".format(error_str))
        

