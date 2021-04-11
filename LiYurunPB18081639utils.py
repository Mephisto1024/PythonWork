# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:12:57 2021

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


class biqugeCrawl():

    m_url = "http://www.biquge.tv/"

	 # search book function
    def search_book(self):
        serach_url = "http://www.biquge.tv/modules/article/search.php?searchkey={}"

        name = input("Please input the book name：")

        name = parse.quote(name.encode('gbk'))

        url = serach_url.format(name)

        response = requests.get(url=url, headers=self.__random_ua())

        root = etree.HTML(response.content)

        try:
            book_name = root.xpath('//*[@id="nr"]/td[1]/a/text()')[0]

            book_author = root.xpath('//*[@id="nr"]/td[3]/text()')[0]

            book_url = root.xpath('//*[@id="nr"]/td[1]/a/@href')[0]

            return [book_name, book_author, book_url]

        except:
            return None

    # download function
    def download(self, book_name, url):
        response = requests.get(url=url, headers=self.__random_ua())
        root = etree.HTML(response.content)

        content_urls = list(map(lambda x: "http://www.biquge.tv/" + x, root.xpath('//*[@id="list"]/dl/dd/a/@href')[9:]))
        content_names = root.xpath('//*[@id="list"]/dl/dd/a/text()')[9:]

        # Create a folder named after the title of the book
        path = '《' + book_name + '》'
        if not os.path.exists(path):
            os.mkdir(path)

        utls_names = [i for i in zip(content_urls, content_names)]

        pool = Pool(processes=5)
        pool.map(self.parse, utls_names)

        print("《{}》Download complete!".format(book_name))


    # Crawling book content function
    def parse(self, url_name):
        url = url_name[0]
        name = url_name[1]

        try:
            response = requests.get(url=url, headers=self.__random_ua())
            html = response.content.decode('gbk')
    
            root = etree.HTML(response.content)
            book_name = root.xpath('//div[@class="con_top"]/a[2]/text()')[0]
    
            content = "".join(re.findall('<div id="content">(.*?)</div>', html, re.S))
    
            content = re.sub("<.*?>", "", re.sub("&nbsp;&nbsp;", " ", content))

            # Create document object
            document = Document()

            # Write text to document
            document.add_paragraph(content)

            document.save("《{}》/《{}》.docx".format(book_name, name))

            print('《' + name + '》Download completed')

        except Exception as e:
            with open("./log.txt", "a+", encoding="utf-8") as file:
                file.write("*"*30+"\n"+str(e))
            print("Exception, Download interrupted, please check the log file！")
            pass

    # random UA
    def __random_ua(self):
        UA = ["Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
              "Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot;Gecko/20100101 Firefox/38.0",
              "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
              "Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0",
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0",
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
              "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
              "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
              "Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/20.6.14",
              "Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
              "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
              "Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; Gecko/20100101 Firefox/38.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
              ]

        headers = {
            "User-Agent": {}
        }

        headers["User-Agent"] = random.choice(UA)

        return headers
