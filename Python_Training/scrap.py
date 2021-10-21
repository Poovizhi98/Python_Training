# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:44:06 2019

@author: psabapathi
"""

import requests
from bs4 import BeautifulSoup

page=requests.get('https://github.com/trending')

#Create a BeautifulSoup object
soup=BeautifulSoup(page.text,'html.parser')

#Get the repo list
repo=soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

#find all instances of that class
repo_list=repo.find_all(class_="Box-row")

print(len(repo_list))