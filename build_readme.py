#!/usr/bin/env python3
import xml
import urllib.request
import xml.etree.ElementTree as ET

BLOG_URL = "http://www.xkyle.com"
RSS_URL = f"{BLOG_URL}/index.xml"


def get_blog_rssxml():
    with urllib.request.urlopen(RSS_URL) as response:
        return response.read()


def print_blog_posts():
    rssxml = get_blog_rssxml()
    root = ET.fromstring(rssxml)
    print(f"Recent [blog]({BLOG_URL}) posts:\n")
    for item in root[0].findall("item")[:5]:
        url = f"{BLOG_URL}{item.find('link').text}"
        text = item.find("title").text
        print(f"* [{text}]({url})")


def print_badge():
    print(
        """
![Build README](https://github.com/solarkennedy/solarkennedy/workflows/Build%20README/badge.svg)
"""
    )


if __name__ == "__main__":
    print_blog_posts()
    print_badge()
