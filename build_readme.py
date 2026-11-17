#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Local RSS feeds from the sibling blog checkouts on this machine
CASCADE_XML = "../kyle.cascade.family/pages/index.xml"
XKYLE_XML = "../xkyle.com/pages/index.xml"

# xkyle.com's RSS uses relative links, so prefix the base URL
XKYLE_BLOG_URL = "https://www.xkyle.com"
CASCADE_BLOG_URL = "https://kyle.cascade.family"


def print_blog_posts(xml_path, post_base_url=""):
    with open(xml_path, "rb") as f:
        root = ET.fromstring(f.read())
    for item in root[0].findall("item")[:5]:
        url = f"{post_base_url}{item.find('link').text}"
        text = item.find("title").text
        print(f"* [{text}]({url})")


if __name__ == "__main__":
    print(f"Recent [blog]({CASCADE_BLOG_URL}) posts:\n")
    print_blog_posts(CASCADE_XML)
    print_blog_posts(XKYLE_XML, XKYLE_BLOG_URL)
