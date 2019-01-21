#!/usr/bin/env python3
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<!doctype html>
    <head>
    </head>
    <body>
        <h1>This is a title.</h1>
        <p class="subtitle">
           Veganism makes me happy! But I'm not the type to preach to people about it.
        </p>
        <p>
            Soda is a poison!
        </p>
        <ul>
            <li>klaus</li>
            <li>elijah</li>
            <li>marcellus</li>
            <li>rebekah</li>
        </ul>
    </body>
</html>'''


simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
print(type(simple_soup))
def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)

def find_list_items():
   list_items = simple_soup.find_all('li')
   list_contents = [e.string for e in list_items]
   print(list_items)
   print(list_contents)

def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)

def find_other_paragraph():

    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)
    
    
    
find_title()
find_list_items()
find_subtitle()
find_other_paragraph()
