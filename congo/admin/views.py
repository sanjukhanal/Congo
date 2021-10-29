from datetime import date

from flask import Blueprint, render_template
from flask_login import login_required

from congo.cart.models import Cart

blueprint = Blueprint("admin", __name__, url_prefix="/admin", static_folder="../static")


@blueprint.route("/")
@login_required
def home():
    """List members."""

    carts = Cart.query.filter(Cart.is_submitted.is_(True), Cart.updated_on >= date.today())
    checkouts = [
        cart.checkouts for cart in carts
    ]
    return render_template("admin/home.html", checkouts=checkouts)
