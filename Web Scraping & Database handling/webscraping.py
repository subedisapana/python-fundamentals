#pip install requests
#pip install BeautifulSoup4  in command line

'''
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser.
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://covid19.mohp.gov.np/")
#print(response.content)
print(response.status_code)

print("--------------------------------------")


soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify()) # add proper indentation


print("--------------------------------------")

'''

Methods:
find('a') #anchor tags
find_all("div") # for division
find_all("img")
find_parent("a")
'''


card = soup.find("div", attrs={"class":"ant-card-grid ant-card-grid-hoverable"})
print(card)

num = card.find("span", attrs={"class":"ant-card-grid ant-card-grid-hoverable"})
print(num.text)
#print(num.text.strip("\n"))
#data = "{} {}  {}". format()
#print(data)