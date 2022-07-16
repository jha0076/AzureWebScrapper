#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS(PMID):

	# url of rss feed
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id='+PMID+'&tool=my_tool&email=my_email@example.com&retmode=xml'

	# creating HTTP response object from given url
	resp = requests.get(url)

	# saving the xml file
	with open(PMID+'.xml', 'wb') as f:
		f.write(resp.content)
		

def parseXML(xmlfile):

	# create element tree object
	tree = ET.parse(xmlfile)

	# get root element
	root = tree.getroot()

	# create empty list for news items
	newsitems = []

	# iterate news items
	for authors in root.findall('./PubmedArticle/MedlineCitation/Article/AuthorList'):

		# empty news dictionary
		news = {}
		authCount = 1
		# iterate child elements of item
		for author in authors:
			affCount = 1
			authorName = author.findall('ForeName')[0].text + ' ' +author.findall('LastName')[0].text
			news['author'+str(authCount)+'_name'] = authorName
			countries = []
			for child in author.findall('AffiliationInfo'):
					news['author'+str(authCount)+'_aff'+str(affCount)] = child[0].text
					countryEmail = child[0].text.split(',')[-1].split('.')
					if len(countryEmail) > 2:
						country = countryEmail[0].strip()
						email = '.'.join(countryEmail[1:]).strip()
						news['author'+str(authCount)+'_aff'+str(affCount)+'_Country'] = country
						countries.append(country)
						news['author'+str(authCount)+'_aff'+str(affCount)+'_Email'] = email
					else:
						news['author'+str(authCount)+'_aff'+str(affCount)+'_Country'] = countryEmail[0].strip()
						countries.append(countryEmail[0].strip())
					affCount += 1
			news['author'+str(authCount)+'_country'] = set(countries).pop()
			authCount += 1
		# append news dictionary to news items list
		newsitems.append(news)
	
	# return news items list
	return newsitems


def savetoCSV(newsitems, filename):

	# specifying the fields for csv file
	fields = newsitems[0].keys()

	# writing to csv file
	with open(filename, 'w') as csvfile:

		# creating a csv dict writer object
		writer = csv.DictWriter(csvfile, fieldnames = fields)

		# writing headers (field names)
		writer.writeheader()

		# writing data rows
		writer.writerows(newsitems)

	
def main():
	PMIDS = ['30410033']
	for PMID in PMIDS:
		# load rss from web to update existing xml file
		loadRSS(PMID)

		# parse xml file
		newsitems = parseXML(PMID+'.xml')

		# store news items in a csv file
		savetoCSV(newsitems, PMID+'.csv')
	
	
if __name__ == "__main__":

	# calling main function
	main()
