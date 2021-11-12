from flask import Blueprint, jsonify, session, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from .forms import CheckoutForm
from .models import Checkout
from ..cart.models import Cart
from ..utils import flash_errors

blueprint = Blueprint("checkout", __name__, url_prefix="/checkout", static_folder="../static")


@blueprint.route("/add_book/<int:book_id>", methods=['POST'])
@login_required
def add_book(book_id):
    """List members."""
    cart_id = session.get("cart_id")
    if cart_id is None:
        cart = Cart.create(
            user_id=current_user.id
        )
        session["cart_id"] = cart.id
    else:
        cart = Cart.get_by_id(cart_id)

    checkout = Checkout.create(
        cart_id=cart.id,
        book_id=book_id,
    )

    return jsonify({"data": {
        "cart_id": cart.id,
        "book_id": book_id,
        "id": checkout.id
    }})


@blueprint.route("/remove_book/<int:checkout_id>", methods=['GET', 'POST'])
@login_required
def remove_book(checkout_id):
    checkout = Checkout.get_by_id(checkout_id)
    checkout.delete()
    flash("You deleted the item.", "success")
    return redirect(url_for('checkout.home'))


@blueprint.route("/", methods=['GET', 'POST'])
def home():
    cart_id = session.get("cart_id")
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        checkouts = cart.checkouts
        total = sum([item.book.price for item in checkouts])
        return render_template("checkout/home.html", checkouts=checkouts, total=total)
    return redirect(url_for('user.home'))


@blueprint.route("/submit", methods=['GET'])
@login_required
def submit():
    cart_id = session.get("cart_id")
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        cart.update(is_submitted=True)
        session.pop("cart_id")
        return render_template("checkout/thank_you.html")
    return redirect(url_for('user.home'))


@blueprint.route("/credit_card", methods=['GET', 'POST'])
@login_required
def credit_card():
    form = CheckoutForm()
    cart_id = session.get("cart_id")
    checkouts=None
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        checkouts = cart.checkouts
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('checkout.submit'))
    flash_errors(form)
    return render_template("checkout/credit_card.html", form=form,  checkouts=checkouts,)
