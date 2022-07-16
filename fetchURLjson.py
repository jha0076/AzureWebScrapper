from bs4 import BeautifulSoup
#from lxml import etree
import requests
# import simplejson as json
import json

f= open(r'C:\Users\HI\Desktop\phamax\GooGleFierce\NewsUpdategoggle.json')
data = json.load(f)
csvHeader = ['Title', 'url', 'Address', 'Service provided',"Add new headers here"]
csvData = []
for row in data:
    URL = r'https://www.nhsinform.scot' + requests.utils.quote(row['url'])
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content,"html.parser")
    csvData.append([row['url'],])
f.close()