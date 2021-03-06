import json

from house_search.scraper import RightMoveScraper, ZooplaScraper

with open("config.json") as f:
    config = json.load(f)


scrapers = [
    RightMoveScraper(),
    # ZooplaAPIScraper(config["zoopla_key"]),
    ZooplaScraper()
]

if __name__ == '__main__':
    location = "Cambridge"
    rentals = []
    for scraper in scrapers:
        rentals += scraper.get_cambridge_rentals()
    rentals = filter(lambda x: x.bedrooms is None or x.bedrooms >= 2, rentals)
    rentals = sorted(rentals, key=lambda x: x.price)
    for rental in rentals:
        print(rental)
