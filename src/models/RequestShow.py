import requests


class RequestShow:
    __base_url = "https://api.tvmaze.com"
    __show_url = f"{__base_url}/search/shows?q="
    __episodes_url = f"{__base_url}/shows/"

    def name(self, term: str):
        query = f"{self.__show_url}{term}"
        return self.__fetch(query)

    def episodes(self, tv_show):
        show_id = tv_show['show']['id']
        query = f"{self.__episodes_url}{show_id}/episodes"
        return self.__fetch(query)

    @staticmethod
    def __fetch(query: str):
        res = requests.get(query)
        return res.json()
