#Made by Ongezell at Ongezell.com

import requests
import json

def get_image_urls(movie_name):
    api_key = "Insert your apiKey here "
    search_engine_id = " Insert your Custom Search Engine ID here"

    query = movie_name + " movie poster"

    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}&searchType=image"
    response = requests.get(url)
    data = response.json()
    image_urls = []
    for i in range(5):
        image_urls.append(data["items"][i]["link"])
    return image_urls

def choose_image_url(image_urls):
    print("Link Broken, Choose an image from the options below:")
    for i, image_url in enumerate(image_urls):
        print(f"{i+1}: {image_url}")
    choice = int(input("Enter your choice (1-5): "))
    return image_urls[choice-1]

def generate_html(name, rating, image_url):
    html = f'<li class="movie" onmouseover="showImage(this)" onmouseout="hideImage(this)" data-image-url="{image_url}" data-rating="{rating}">\n'
    html += f'  <span class="name">{name}</span>\n'
    html += f'  <span class="rating">{rating}</span>\n'
    html += '</li>\n'
    html += f'<img class="moveAble" src="{image_url}" alt="Movie image">\n'
    return html

def main():
    num_movies = int(input("Enter the number of movies: "))
    html = ""
    for i in range(num_movies):
        name = input("Enter the name of the movie: ")
        rating = input("Enter the rating of the movie: ")
        image_urls = get_image_urls(name)
        image_url = choose_image_url(image_urls)
        html += generate_html(name, rating, image_url)
    with open("movies.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    main()
