import bleach
from flask_wtf import FlaskForm
from sqlalchemy import or_

from congo.book.models import Book


class SearchForm(FlaskForm):

    def __init__(self, query_string=None, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.books = None
        if query_string:
            self.query_string = bleach.clean(query_string)
        else:
            self.query_string = ''
        if self.query_string:
            self.books = Book.query.filter(
                or_(
                    Book.title.ilike(f"%{self.query_string}%"),
                    Book.description.ilike(f"%{self.query_string}%"),
                )
            )
        else:
            self.books = Book.query.all()
