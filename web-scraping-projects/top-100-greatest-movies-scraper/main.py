import requests
from bs4 import BeautifulSoup

# Send a GET request to the specified URL to fetch the webpage content
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Select all movie titles from the article section
# The selector targets <strong> tags inside <h2>, which are within <span>, <div>, and <article>
movies_article = soup.select(selector="article div span h2 strong")

# Extract the text of each movie tag, reverse the order, and store in a list
movies_text = [tag.getText() for tag in reversed(movies_article)]

# Iterate through the list of movie titles
for movie in movies_text:
    # Open (or create) a file called "movies.txt" in append mode
    # Write each movie title to the file, each on a new line
    with open(file="movies.txt", mode="a+") as file:
        file.write(f"{movie}\n")
