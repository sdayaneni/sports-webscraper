#Import all libraries for project
from bs4 import BeautifulSoup
import requests
from googlesearch import search

#Goes to ESPN and find headlines on the homepage
content = requests.get('https://www.espn.com/').text
soup = BeautifulSoup(content, 'lxml')
headlineSection = soup.find('section', class_ = 'col-three')
filtered = headlineSection.find('ul', class_='headlineStack__list')
headlines = filtered.find_all('li')
secondInstance = filtered.text

allLinks = filtered.find_all('a')
espnLinks = []
googleLinks = []

#Gets links for headlined articles on ESPN homepage and generates google search results based on headlines
for i in range (len(headlines)):
    print(headlines[i].text)
    currentLink = allLinks[i]
    espnLinks.append('http://espn.com' + currentLink['href'])
    googleLinks.append(search(headlines[i].text, num_results = 3, lang = "en"))

print(' ')
print(googleLinks[0])
print(' ')

#Prints out headline and links ESPN article for reference
for i in range(len(espnLinks)):
    nextContent = requests.get(espnLinks[i]).text
    nextSoup = BeautifulSoup(nextContent, 'lxml')
    preview = nextSoup.find('p').text
    print('"' + preview + '"'+ "Check out-----" + espnLinks[i] + "-----to learn more.")
    print(' ')

#Scrapes first picture available for headline in websites based on google search
findPictures = None
print(' ')
while(findPictures) == None:
    linkNumber = 0
    searchNumber = 0
    currentSearch = googleLinks[searchNumber]
    googleWebsiteContent = requests.get(currentSearch[linkNumber]).text
    soupForPictures = BeautifulSoup(googleWebsiteContent, 'lxml')
    findPictures = soupForPictures.find('img')['src']
    linkNumber = linkNumber + 1
    searchNumber = searchNumber + 1
    print(findPictures)

#Put content into textfile
textFile = open("C:\Programming\Dev\Practice\Projects\sportsWebScraper\content.txt", "w")
for i in range (len(headlines)):
    textFile.write(headlines[i].text)
    textFile.write("\n")
textFile.write("\n")
for i in range(len(espnLinks)):
    nextContent = requests.get(espnLinks[i]).text
    nextSoup = BeautifulSoup(nextContent, 'lxml')
    preview = nextSoup.find('p').text
    textFile.write('"' + preview + '"'+ "Check out-----" + espnLinks[i] + "-----to learn more.")
    textFile.write('\n')
textFile.close()
