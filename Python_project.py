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
