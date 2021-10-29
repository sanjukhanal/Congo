from flask import Blueprint, render_template
from flask_login import login_required

from .forms import SearchForm
from .models import Book

blueprint = Blueprint("book", __name__, url_prefix="/book", static_folder="../static")


@blueprint.route("/<int:book_id>", methods=['GET'])
@login_required
def book_detail(book_id):
    book = Book.get_by_id(book_id)
    if book:
        return render_template("book/book_detail.html", book=book)
