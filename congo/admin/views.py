import datetime
from datetime import date, datetime, timedelta

from flask import Blueprint, render_template, session, abort, request
from flask_login import login_required

from congo.admin.forms import DateToggle
from congo.cart.models import Cart
from congo.user.models import User

blueprint = Blueprint("admin", __name__, url_prefix="/admin", static_folder="../static")


@blueprint.route("/", methods=['GET', 'POST'])
@login_required
def home():
    """List members."""
    user_id = session.get("user_id", None)
    if user_id:
        form = DateToggle()
        user = User.get_by_id(user_id)
        if user and user.is_admin:
            updated_on = date.today().replace(year=1970, month=1, day=1)
            utc_now = datetime.utcnow()
            if request.method == "POST" and form.validate_on_submit():
                if form.reports_for.data == "yesterday":
                    updated_on = utc_now - timedelta(days=1)
                elif form.reports_for.data == "this_month":
                    updated_on = utc_now.replace(day=1)
                elif form.reports_for.data == "last_month":
                    updated_on = utc_now.replace(month=date.today().month - 1)
                elif form.reports_for.data == "current_year":
                    updated_on = utc_now.replace(month=1, day=1)
                else:
                    updated_on = utc_now.replace(year=1970, month=1, day=1)
            carts = Cart.query.filter(Cart.is_submitted.is_(True), Cart.updated_on >= updated_on)
            checkouts = [
                cart.checkouts for cart in carts
            ]
            return render_template("admin/home.html", checkouts=checkouts, form=form)
    return abort(401)
