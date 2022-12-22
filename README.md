# Movie List Editor

Made this "web app" to help me organize my [movie list](https://ongezell.com/blogposts/movies.html) on my blog, releasing it because maybe it ends up being something useful for someone else.
This script allows you to create a list of movies, along with their ratings and associated images. The images are obtained through a Google Custom Search API.

## How to use

1. Replace the `apiKey` and `searchEngineId` variables at the top of the script with your own API key and search engine ID.
2. In the `main` function, enter the number of movies you want to include in the list.
3. For each movie, enter its name and rating. The script will automatically retrieve a list of image options from the Google Custom Search API, and display them in a horizontal row.
4.The script finds the cover image for it automatically but if fails it will prompt you to pick one from five images by clicking on it. The selected image will be highlighted with a green border.
5. When you have selected an image for all movies, the script will generate the HTML code for the movie list and display it in a `div` element at the end of the page.

## How to generate an API key and a search engine ID

1. Go to here [Custom-search Introduction](https://developers.google.com/custom-search/v1/introduction).
2. Click on receive key.
3. Select or create project > Create
4. Name Project > Next
5. Click the "Enable" button.
6. Copy your Key and use it on the script.

For the search engine ID follow these steps.

1. Go here [Programmable Search Engine Panel](https://developers.google.com/custom-search/v1/introduction).
2. Give a name to your search engine.
3. Select "Search the entire web"
4. Activate "Search for Images"
5. You will get a embed code, copy the numbers showed bellow. That's your ID
![ID](https://i.imgur.com/sJtuQEl.png)

