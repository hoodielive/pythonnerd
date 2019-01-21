#!/usr/bin/env python3
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<!doctype html>
<html class="no-js" lang="">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <title>Beautiful Soup</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="apple-touch-icon" href="/apple-touch-icon.png">
        <!-- Place favicon.ico in the root directory -->

    </head>
    <body>
        <!--[if lt IE 8]>
            <p class="browserupgrade">
            You are using an <strong>outdated</strong> browser. Please
            <a href="http://browsehappy.com/">upgrade your browser</a> to improve
            your experience.
            </p>
        <![endif]-->
        <h1>This is a title.</h1>
        <p class="subtitle">
            Non sodales neque sodales ut etiam sit amet nisl purus? Elit, at imperdiet dui accumsan sit
            amet nulla facilisi morbi tempus iaculis urna, id volutpat lacus laoreet non curabitur gravida!
        </p>
        <ul>
            <li>Klaus</li>
            <li>Elijah</li>
            <li>Marcellus</li>
            <li>Rebekah</li>
        </ul>
    </body>
</html>'''


simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    print(simple_soup.string('h1'))
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)

def find_list_items():
   list_items = simple_soup.find_all('li')
   print(list_items)

find_title()
find_list_items()
