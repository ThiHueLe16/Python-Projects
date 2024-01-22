import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
content=requests.get(URL).text
soup=BeautifulSoup(content, "html.parser")
top100Movie=[movie.getText() for movie in soup.find_all(name="h3", class_="title")]
print(top100Movie[::-1])
with open("top100Movie.txt", "a") as file:
    for movie in top100Movie[::-1]:
        file.write(movie +"\n")