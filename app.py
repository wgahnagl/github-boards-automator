import yaml
import requests 
from bs4 import BeautifulSoup

def main():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)[0]
        query = []
        for item in config["query"].split():
            item = item.replace("/", "%2F")
            query.append(item)
        query = "%20".join(query)
        board_name = config["columns"][0]["name"]
        request_url = 'https://api.github.com/search/issues?q=' + query
        request = requests.get(request_url)
main()
