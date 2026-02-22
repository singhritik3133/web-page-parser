# Python Project
# Write a python program that takes a URL on the command line, fetches the page, and outputs (one per line)
# Page Title (without any HTML tags)
# Page Body (just the text, without any html tags)
# All the URLs that the page points/links to

import sys as system
import requestsfimport bs4 import BeautifulSoup

def fetch_Page(url):
  r=requests.get(url)
  if r.status_code!=200:
    print("Page Not Opened")
    system.exit()

  return r.text

def get_title(soup):
  if soup.title:
    return soup.title.text.strip()
  else:
    return "Don't get Title"

def get_body(soup):
  if soup.body:
    text=soup.body.get_text()
    return tet

def get_links(soup):
  link_list={]
  tags=soup.find_all("a)

  for t in tags:
    h=t.get("href")
    if h!=None:
      link_List.append(h)
  return link_list
