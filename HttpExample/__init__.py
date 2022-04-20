import logging

from selenium.webdriver.chrome.options import Options
import azure.functions as func
from selenium import webdriver
# from azure.identity import DefaultAzureCredential, ClientSecretCredential
# from azure.storage.blob import BlobServiceClient
from datetime import date
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import simplejson as json
#Taking the neceessary imports

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request. 11:38')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    driver = webdriver.Chrome(options=chrome_options)
    # List will contain all the information extracted information after each iteration
    thislist = []
    # the format for Amgen is dd.mm.yyyyy
    today = date.today()
    # Today's date is calculated in the format dd.mm.YY 
    subs = [today.strftime("%d.%m.%Y")]
    key =["Mimpara"]
    #Calling the Amgen site 
    driver.get('https://www.amgen.com/search-results?q='+key[0])
    sleep(10)
    #arranging the articles in order of the date
    tap=driver.find_element_by_id("CybotCookiebotDialogBodyButtonAccept")   
    tap.click()
    sleep(1)
    try:
         nextp=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-custom-select")) 
     ) 
    
         nextp.click()
    
    
    except:
     driver.quit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-custom-select")) 
     ).send_keys(Keys.DOWN)
    nextp.send_keys(Keys.ENTER)  

    data=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quantum-search-list")) 
     ) 

    
    data2=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quantum-search-link")) 
     )  
    # Counter to keep record for each newsitem if there is 
    # no news of that 
    # particular day it prints no news using this counter's value
    c=0
    for ele,ele2 in zip(data2,data):
        quote={}
        quote['Date']=ele2.text[:10]
        quote['NewsUpdate']=ele.get_attribute('innerHTML')
        quote['link']=ele.get_attribute('href')
        
        if ele2.text[0:10] in subs:
          c=c+1
          print(quote,c)
          thislist.append(quote)
          filename = 'NewsUpdateAmgen.json'
          jsonString = json.dumps(thislist)
          jsonFile = open(filename, "w")
          jsonFile.write(jsonString)
          jsonFile.close() 
    #if count =0 than it will display the null message      
    if c==0:
     print("No News Update for "+ subs[0]) 
     logging.info("No News Update for "+ subs[0])
     return func.HttpResponse(
             "No News Update for "+ subs[0],
             status_code=200)
 
    else:    
     logging.info(thislist)
    return func.HttpResponse(
             str(thislist),
             status_code=200
    )