#!/usr/bin/env python3
import xml
import urllib.request
import xml.etree.ElementTree as ET

XKYLE_BLOG_URL = "http://www.xkyle.com"
CASCADE_BLOG_URL = "http://kyle.cascade.family"


def get_blog_rssxml(rss_url):
    with urllib.request.urlopen(rss_url) as response:
        return response.read()


def print_blog_posts(blog_url):
    rss_url = f"{blog_url}/index.xml"
    rssxml = get_blog_rssxml(rss_url)
    root = ET.fromstring(rssxml)
    for item in root[0].findall("item")[:5]:
        url = f"{blog_url}{item.find('link').text}"
        text = item.find("title").text
        print(f"* [{text}]({url})")


def print_badge():
    print(
        """
![Build README](https://github.com/solarkennedy/solarkennedy/workflows/Build%20README/badge.svg)
"""
    )


if __name__ == "__main__":
    print(f"Recent blog posts:\n")
    print_blog_posts(CASCADE_BLOG_URL)
    print_blog_posts(XKYLE_BLOG_URL)
    print_badge()
