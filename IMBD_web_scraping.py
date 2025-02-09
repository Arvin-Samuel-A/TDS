import json
import httpx
from lxml import html
from typing import List, Dict

def scrape_imdb() -> List[Dict[str, str]]:
    """Scrape IMDb movies using httpx and lxml, including movie IDs.

    Returns:
        List of dictionaries containing movie title, year, rating, and ID.
    """
    headers = {"User-Agent": "Mozilla/5.0 (compatible; IMDbBot/1.0)"}
    response = httpx.get("https://www.imdb.com/search/title/?user_rating=2,4&count=25", headers=headers)
    response.raise_for_status()

    tree = html.fromstring(response.text)
    movies = []

    for item in tree.cssselect(".ipc-metadata-list-summary-item"):
        title = (
            item.cssselect(".ipc-title__text")[0].text_content()
            if item.cssselect(".ipc-title__text")
            else None
        )
        year = (
            item.cssselect(".dli-title-metadata-item span")[0].text_content()
            if item.cssselect(".cli-title-metadata span")
            else None
        )
        rating = (
            item.cssselect(".ipc-rating-star")[0].text_content()
            if item.cssselect(".ipc-rating-star")
            else None
        )
        # Extract movie ID from the href attribute
        link_element = item.cssselect("a.ipc-title-link-wrapper")
        movie_id = (
            link_element[0].get("href").split("/")[2] 
            if link_element else None
        )
        print(title, year, rating, movie_id)
        if title and year and rating and movie_id:
            movies.append({"id": movie_id, "title": title, "year": year, "rating": rating})

    print(movies)

scrape_imdb()