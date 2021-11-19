import requests


class RequestShow:
    baseUrl = "https://api.tvmaze.com"

    def name(self, term: str):
        res = requests.get(f"{self.baseUrl}/search/shows?q={term}")
        return res.json()[0]

    def episodes(self, show):
        res = requests.get(f"{self.baseUrl}/shows/{show['show']['id']}/episodes")
        return res.json()
