from flask import Blueprint, jsonify, session
from flask_login import login_required, current_user

from .models import Cart

blueprint = Blueprint("cart", __name__, url_prefix="/cart", static_folder="../static")


@blueprint.route("/get_create", methods=['POST'])
@login_required
def get_or_create():
    """List members."""
    cart_id = session.get("cart_id")
    if cart_id is None:
        cart = Cart.create(
            user_id=current_user.id
        )
        session["cart_id"] = cart.id
    else:
        cart = Cart.get_by_id(cart_id)

    return jsonify({"data": {
        "id": cart.id
    }})
