import sys
# import time

import os
from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString # required for HTML and XML parsing                                                              # required for HTML and XML parsing: pip install beautifulsoup4


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'C:\Users\olegs\Desktop\gsoc_publisher\chromedriver_win32\chromedriver.exe',options=chrome_options)


issues_url = "https://github.com/deepmipt/DeepPavlov/issues"

driver.get(issues_url)
htmlSource = driver.page_source

nextSoups = []
for pageNum in range(10):
    driver.get(issues_url+f"?page={pageNum}")
    htmlSource2 = driver.page_source
    soup2 = BeautifulSoup(htmlSource2, features="html.parser")
    nextSoups.append(soup2)

soup = BeautifulSoup(htmlSource, features="html.parser")
content_html = soup.find("div", attrs={"class": "repository-content"})

e = soup.find("div", attrs={"class": "bg-gray-light pt-3 hide-full-screen mb-5"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "position-relative js-header-wrapper "})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "position-relative js-header-wrapper"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "js-pinned-issues-reorder-container"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "paginate-container d-none d-sm-flex flex-sm-justify-center"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "footer container-xl width-full p-responsive"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "protip"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "paginate-container d-sm-none mb-5"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "Box-header d-flex flex-justify-between"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "ml-2 pl-2 d-none d-md-flex"})
if e:
    e.extract()
e = soup.find("div", attrs={"class": "ml-3 d-flex flex-justify-between width-full width-md-auto"})
if e:
    e.extract()

c3s = []
for soup2 in nextSoups:
    for c in soup2.findAll("div", attrs={"aria-label": "Issues"}):
        # print(type(c))
        for c2 in c.findAll("div", attrs={"class": "js-navigation-container js-active-navigation-container"}):
            for c3 in c2.children:
                c3s.append(c3)


for c3 in c3s:
    soup.find("div", 
              attrs={"class": "js-navigation-container js-active-navigation-container"})\
              .append(c3)
                # print(c3)

soup_pretty = str(soup)

soup_pretty = soup_pretty.replace('"/deepmipt/DeepPavlov/issues', '"https://github.com/deepmipt/DeepPavlov/issues')
soup_pretty = soup_pretty.replace('"/users', '"https://github.com/users')

import os
os.makedirs("_includes", exist_ok=True)
with open("_includes/gsoc_ideas.html", 'w', encoding="utf-8") as f:
    print(soup_pretty, file=f)

