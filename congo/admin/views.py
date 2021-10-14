from flask import Blueprint, render_template
from flask_login import login_required

from congo.book.nyt import BEST_SELLERS

blueprint = Blueprint("admin", __name__, url_prefix="/admins", static_folder="../static")


@blueprint.route("/")
@login_required
def home():
    """List members."""
    best_sellers = BEST_SELLERS
    return render_template("admin/home.html", best_sellers=best_sellers)
