import requests
import sys
import ast

#movieTitle = (sys.stdin.readline()).replace(" ", "_") + ","
movieTitle = "Avatar_the_way_of_water"
url = "https://www.rottentomatoes.com/m/" + movieTitle.lower()
response = requests.get(url)
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')
current_string1 = " ".join(map(str,soup))
current_string1 = current_string1[current_string1.find('"genre":'):]
#finding genres
temp_text = current_string1[current_string1.find('"genre":')+8: current_string1.find(']')] + ']'
current_string1 = current_string1[current_string1.find('"upright","score":'): current_string1.find('"audienceClass":"upright","score":') + 50]
rating = current_string1[current_string1.find(':')+1:current_string1.find(':')+3]
#genre list for the content
genre_list = ast.literal_eval(temp_text)
movieTitle += ";,"
for genre in genre_list:
    movieTitle = movieTitle + " " + genre + ","

print(movieTitle)