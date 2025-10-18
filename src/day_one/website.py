import requests
from bs4 import BeautifulSoup


class Website:

    url: str
    title: str
    text: str

    def __init__(self, url):
        self.url = url

    def webscrape(self):
        response = requests.get(self.url,timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No String found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
