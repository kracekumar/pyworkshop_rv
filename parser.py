# -*- coding: utf-8 -*-

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


if __name__ == "__main__":
    content = """<html>
    <head>
    <title> Movie listing </title>
    </head>
    <body>
    <div>
        <a href="pulp_fiction.html">Pulp Fiction</a>
        <a href="shaswank_redemption.html">Shaswank Redemption</a>
    </div>
    </body>
    </html>
    """
    p = HTMLParser()
    p.feed(content)
    p.close()
    print p.links

    url = URLLister()
    url.feed(content)
    url.close()
    print url.urls
