"""This file contains instructions for the workshop and code.
"""

# Step1: run `python -m SimpleHTTPServer 8000` from current directory.
# Step2: Go to `http://localhost:8000` in the browser
# Step3: Try hands on with python interpreter like variables, string, expressions
# Step 4: Fetch the contents available in http://127.0.0.1:8000/
# Step 5: Extract all links in the page and store in the variable `links`.
# Step 6: Create a function called `extract_links` ad move the above logic.
# Step 7: Extract contents in each page and store content in the variable `contents`
# Step 8: Extract movie details in the page and store each movie details in list
# `movie_details`. Store each movie detail in dict.
# Step 9: Store the each movie details in separate file like `pulp_fiction.json`
# Step 10: Read the details back from file and print.
# Step 11: Create a class called Movie which store movie details.
# Step 12: Given a filename Movie class should be able to read the file and
# assign to attributes.
# C:\Python27\python.exe main.py
from sgmllib import SGMLParser


class HTMLParser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.links = []
        self.spans = []
        self.record_data = False
        self.legend = None

    def handle_data(self, data):
        if self.record_data:
            self.spans.append({self.legend: data})

    def start_a(self, attributes):
        href = [v for k, v in attributes if k == 'href']
        if href:
            self.links.extend(href)

    def start_span(self, attrs):
        for k, v in attrs:
            self.legend = v
        self.record_data = True

    def end_span(self):
        self.record_data = False


def get_all_links(text):
    p = HTMLParser()
    p.feed(text)
    p.close()
    return p.links


def get_all_spans(text):
    p = HTMLParser()
    p.feed(text)
    p.close()
    return {k: v for item in p.spans for k, v in item.items()}

def get_content_from_url(url):
    resp = urllib.urlopen(url)
    content = resp.read()
    resp.close()
    return content


import urllib

site = "http://localhost:8000"

content = get_content_from_url(site)
urls = get_all_links(content)

urls[0] = "http://localhost:8000/pulp_fiction.html"
contents = []
for url in urls:
    if not url.startswith('http'):
        url = site + "/" + url
    contents.append(get_content_from_url(url))

movie_details = []
for content in contents:
    details = get_all_spans(content)
    movie_details.append(details)

filename = 'movies.txt'
f = open(filename, 'w')
for detail in movie_details:
    for k, v in detail.items():
        f.write(k + ":" + v + "\n")
f.close()
with open(filename) as f:
    for line in f:
        print line,
