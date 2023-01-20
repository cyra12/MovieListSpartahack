import requests
import sys
import ast


#makes movie title url friendly
movieTitle = (sys.stdin.readline()).replace(" ", "_").replace("\n","")
#movieTitle = "Wall E".replace(" ", "_")

# the url for any given movie (so far as I can tell, if theres an issue there I will be very put out)
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

#If the url doesnt take you anywhere cry
try:
    genre_list = ast.literal_eval(temp_text)
except:
    exit()

movieTitle = movieTitle.replace("_", " ")
movieTitle += ";,"
for genre in genre_list:
    movieTitle = movieTitle + " " + genre + ","

print(movieTitle + "\\n")