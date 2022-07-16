from tkinter import E
from bs4 import BeautifulSoup
from lxml import etree
import requests
import simplejson as json


quotes=[] 
#KEYWORD = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
KEYWORD = ["1"]
count=0
for i in KEYWORD:
 URL = "https://www.nhsinform.scot/scotlands-service-directory/health-and-wellbeing-services?sortby=_distance&sortdir=Asc&svctype=51&page="+i
#PARSE_MDATE_FP = "October 16,2016"
# for each key word
# Fetch the result -> define the date -> 
 count+=1
 HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

 webpage = requests.get(URL, headers=HEADERS)
 soup = BeautifulSoup(webpage.content,"html.parser")
#print(soup)
  # a list to store news quotes
   
 #table = soup.findAll('div', attrs={'class':'g'}),

 def getInnerURL(quote):
    try:
        HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
        innerWebpage = requests.get(quote['url'], headers=HEADERS)
        innerSoup = BeautifulSoup(innerWebpage.content,"html.parser")
        #Write all the code 
        dom= etree.HTML(str(innerSoup))

        isOpenPath = "/html/body/main/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/h3"
        isOpen = dom.xpath(isOpenPath)[0].text
        if isOpen != '':
            contactNumberPath = "//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[3]/div[3]/div[3]/div/div[1]/dl[1]/dd"
        else:
            contactNumberPath = "/html/body/main/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div[1]/dl/dd"
        contactNumber = dom.xpath(contactNumberPath)[0].text
        
        quote['contactNumber'] = ' '.join(contactNumber.replace("\n","").replace("\r","").split())

        mapPath = "/html/body/main/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/div/a/@href"
        mapPath2= "/html/body/main/div[2]/div[2]/div[1]/div[3]/div[3]/div[4]/div/a/@href"
        map = dom.xpath(mapPath)[0]

        quote['Map'] = map

    except Exception as e:
        print(e)

    #return [contactNumber,map]

 for row in soup.findAll('li', attrs={'class':'search__item search__item--ssd'}):
     quote = {}
     print(row)
    
     print("---")
     quote['Title'] = ' '.join(row.h3.text.replace("\n","").replace("\r","").split())

     quote['url'] = (r'https://www.nhsinform.scot'+requests.utils.quote(row.a['href']).strip())

     urlResults = getInnerURL(quote)
     quote['Address'] =  ' '.join(row.address.text.replace("\n","").replace("\r","").split())
    
     quote['Service provided'] = ' '.join(row.p.text.replace("\n","").replace("\r","").split())

     quotes.append(quote)
     print(count)
     
#print(quotes)
filename = 'NewsUpdategoggle.json'
jsonString=json.dumps("goggle")   
jsonString = json.dumps(quotes)
jsonFile = open(filename, "w")
jsonFile.write(jsonString)
jsonFile.close()   

    #use the file extension .json
 # retrieving  article
#url = soup.find('article').find_all('a')
#print(paragraphs)
#for paragraph in paragraphs:
 #   print (paragraph.text)

#title = soup.find_all("article")
#link = soup.find( "a", attrs={'class': 'href'})
 
# Inner NavigableString Object

#for i in title: 
         
#  print (''.join(title.findAll(text=True)))
 
    # saving the article in the file
#File.write(f"{title_string},")
 
    # retrieving price

#link = soup.find( "a")
                                
        
#print (link)
 
    # saving
    #File.write(f"{price},")
 
#Article= soup.find_all("article")
#for i in  Article:
#    print (''.join(i.findAll(text=True)))
        
#    link=soup.find_all("h2")
#    print (''.join(link.findAll(text=True)))

#for link in soup.find_all('a'):
 #   print(link.get('href'))
#for node in soup.find_all("time"):
#   print (''.join(node.findAll(text=True)))


