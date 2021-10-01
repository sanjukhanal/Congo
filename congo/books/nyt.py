from functools import cached_property

from pynytimes import NYTAPI

from settings import NYT_KEY


class BookApi(NYTAPI):
    def __init__(self):
        super().__init__(key=NYT_KEY, parse_dates=True)


api = BookApi()
BEST_SELLERS = api.best_sellers_list()
