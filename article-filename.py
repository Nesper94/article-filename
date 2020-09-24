#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  article-filename.py
#  
#  Copyright 2020 Juan C. Arboleda R. <juan.arboleda2@udea.edu.co>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import argparse, requests, bs4, pyperclip

parser = argparse.ArgumentParser(description='Obtener un nombre de archivo a partir de una página web.')
parser.add_argument('web', help='Página web del artículo (enlace de PubMed, tal vez funcione con un enlace de PMC también).')
parser.add_argument('--kebab', help='Usar Kebab case en el nombre del artículo.', action='store_true')

args = parser.parse_args()

# Get article with requests module and convert it to BeautifulSoup object
article = requests.get(args.web)
article = bs4.BeautifulSoup(article.text, 'html.parser')

# Obtain title
title = article.select('meta[name="citation_title"]')[0].get('content')
# Don't use TITLES IN UPPERCASE, THEY ARE SO UGLY
if title.isupper():
    title = title.capitalize()

if args.kebab:
    title = title.replace(' ', '-')

# Obtain authors
authors = article.select('meta[name="citation_authors"]')[0].get('content')

# Obtain publication date and extract the year only

date = article.select('time[class="citation-year"]') # Another way to get the year

for tag in date:
    date = tag.text

if not date:
    date = article.select('meta[name="citation_date"]')[0].get('content')
    print(date)

date = date.split(' ')
date = [i for i in date if i.isnumeric()][0]

# Print article info
print('Authors: ', authors)
print('Title: ', title)
print('Date: ', date)

# The structure of authors until this line is, for example: 'Pham SK;Antipov D;'
authors = authors.split(';')

if len(authors) == 3: # i.e. if it is there only two authors
    
    auth1, auth2 = authors[0], authors[1]
    lastname1, lastname2 = auth1.split(' ')[0], auth2.split(' ')[0]

    # Make sure lastnames are formatted properly
    if lastname1.isupper():
        lastname1 = lastname1.title()
    if lastname2.isupper():
        lastname2 = lastname2.title()
    
    filename = lastname1+'&'+lastname2+'_'+date+'_'+title+'.pdf'
    
else: # One author or more than two authors
    
    author = authors[0] # Obtain only first author
    lastname = author.split(' ')[0] # Get lastname

    # Make sure lastname is formatted properly
    if lastname.isupper():
        lastname = lastname.title()

    if len(authors) < 3:
        filename = lastname+'_'+date+'_'+title+'.pdf'
        
    else:
        filename = lastname+'-et-al_'+date+'_'+title+'.pdf'

print('')
print(filename)
pyperclip.copy(filename)
