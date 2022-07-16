from re import X
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
from bs4 import BeautifulSoup
import simplejson as json
    
s=Service('C:/Users/HI/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.google.com/search?q=site%3Afiercepharma.com+mimpara')
    
sleep(10)
quotes=[]
data=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "jtfYYd")) 
         ) 
            # if el#h1=soup.find_all(\"div\" class_=\"BNeawe s3v9rd AP7Wnd\")\n",
    #print(h1)\n",
    #ee=soup.findAll(\"div\", attrs={\"class\":\"GyAeWb\"})\n",
    #print(ee)\n"
    
for elm in data:
      
      print("---")
      quote = {}
      quote['NewsUpdate']=elm.text[0:]
      quote['link']=elm.get_attribute("href")
      print(quote)
        
      
    #quote['Title'] = row.div[\"BNeawe s3v9rd AP7Wnd\"].text\n
   