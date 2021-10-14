from pynytimes import NYTAPI

from congo.book.models import Book
from congo.settings import NYT_KEY


class BookApi(NYTAPI):
    def __init__(self):
        super().__init__(key=NYT_KEY, parse_dates=True)


api = BookApi()
BEST_SELLERS = api.best_sellers_list()
