from flask import Blueprint
from .models import Book
blueprint = Blueprint("book", __name__, url_prefix="/book", static_folder="../static")
