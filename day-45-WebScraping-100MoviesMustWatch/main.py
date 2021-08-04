import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

response = requests.get(URL)
#print(response)
website_html = response.text
#print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
#print(soup.prettify())

all_movies = soup.select('.titleColumn a')
print(all_movies[1].string)

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")