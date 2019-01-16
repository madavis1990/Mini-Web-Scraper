#! /usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import glob
import sys

for filename in glob.glob('*.html'):
	newfile = filename[:-5]
	newfile += '.txt'
	file = open(newfile,'w')
	sys.stdout = file

	soup = BeautifulSoup(open(filename), "html.parser")
	#scrape email
	imgs = soup.find('img', {'class': 'email-image'})
	emailStart = re.compile(r'user=')
	emailEnd = re.compile(r'&amp;domain')
	emailText = str(imgs)
	array = emailText.split("=")
	emailText = array[3]
	array = emailText.split("&")
	email = array[0]
	email += '@txstate.edu'
	#scrape homepage
	webScrape = soup.find('div', {'class': 'details col-md-9 col-sm-8 col-xs-6'})
	webInfo = webScrape.find('a', {'target': '_blank'})
	webSite =''
	if webInfo:
		webSite = str(webInfo)
		webSites = webSite.split('"')
		webSite = webSites[1]
	else:
		webSite = 'none'
	nameText = soup.find('h3', {'class': 'heading-title pull-left'})
	name = str(nameText)
	names = name.split()
	name = names[3]+' '+names[4]+' '+names[5]
	#scrape interests and education
	divList = []
	divs = soup.findAll('div', {'class': 'panel-body'})
	for div in divs:
		divList.append(str(div))	
	interests = divList[0]
	education = divList[1]

	array = interests.split(">")
	array=array[2].split("<")
	interests = array[0]

	array = education.split(">")
	array=array[2].split("<")
	education = array[0]

	print 'Name: '+name
	print 'Education: '+education
	print 'Research interests: '+interests
	print 'Email: '+email
	print 'Webpage: '+webSite
