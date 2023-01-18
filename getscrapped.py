import requests
import ast
from bs4 import BeautifulSoup
#brute forcing webscrapping and assuming each ImDb page is identical in formatting (we checked and it seems to be)
url = #however we plan to get the url
#add url var instead of the text
page = requests.get('https://www.imdb.com/title/tt4686844/')
# Parse the HTML of the website
soup = BeautifulSoup(page.content, 'html.parser')
#child_soup = soup.find_all('script id="NEXT_DATA" type="application/json"')
current_string1 = " ".join(map(str,soup))
current_string1 = current_string1[current_string1.find('<title>'), current_string1.find("<script>if(typeof uet === 'function'){ uet('be', 'LoadTitle', {wb: 1}); }</script><script>window.addEventListener")]
#finding genres
temp_text = current_string1[current_string1.find('"genre":'), current_string1.find(']'))
rating = int(current_string1.find('ratingValue":'), current_string.find('}'))
#genre list for the content
genre_list = ast.literal_eval(genre_list)

