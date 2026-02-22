# Write a python program that takes a URL on the command line, fetches the page, and outputs (one per line)
# Page Title (without any HTML tags)
# Page Body (just the text, without any html tags)
# All the URLs that the page points/links to

import sys
import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    r = requests.get(url)

    if r.status_code != 200:
        print("Page nahi khula")
        sys.exit()

    return r.text


def get_title(soup):
    if soup.title:
        return soup.title.text.strip()
    else:
        return "No title milaa"


def get_body(soup):
    if soup.body:
        text = soup.body.get_text()
        return text
    else:
        return ""


def get_links(soup):
    link_list = []

    tags = soup.find_all("a")

    for t in tags:
        h = t.get("href")
        if h != None:
            link_list.append(h)

    return link_list


def main():

    if len(sys.argv) < 2:
        print("URL pass karo command line me")
        sys.exit()

    url = sys.argv[1]

    html = fetch_page(url)

    soup = BeautifulSoup(html, "html.parser")

    title = get_title(soup)
    print(title)

    body = get_body(soup)
    print(body)

    links = get_links(soup)

    for l in links:
        print(l)


main()
