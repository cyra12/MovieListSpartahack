# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:14:11 2023

@author: willi
"""
import requests
import ast
from bs4 import BeautifulSoup
#brute forcing webscrapping and assuming each ImDb page is identical in formatting (we checked and it seems to be)
#url = however we plan to get the url
page = requests.get('https://www.rottentomatoes.com/m/christmas_at_the_golden_dragon')
# Parse the HTML of the website
soup = BeautifulSoup(page.content, 'html.parser')
current_string1 = " ".join(map(str,soup))
current_string1 = current_string1[current_string1.find('"genre":'):]
#finding genres
temp_text = current_string1[current_string1.find('"genre":')+8: current_string1.find(']')] + ']'
current_string1 = current_string1[current_string1.find('"upright","score":'): current_string1.find('"audienceClass":"upright","score":') + 50]
rating = current_string1[current_string1.find(':')+1:current_string1.find(':')+3]
#genre list for the content
genre_list = ast.literal_eval(temp_text)
print(rating)
print(genre_list)
