import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.get_text()[:3000]
    except:
        return ""