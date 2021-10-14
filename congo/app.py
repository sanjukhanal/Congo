# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""

import logging
import sys

from flask import Flask, render_template, session

from congo import public, user, admin, cart, checkout, customer, book
from congo.extensions import (
    bcrypt,
    cache,
    csrf_protect,
    db,
    flask_static_digest,
    login_manager,
    migrate,
)


def create_app(config_object="congo.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    flask_static_digest.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(book.views.blueprint)
    app.register_blueprint(checkout.views.blueprint)
    app.register_blueprint(cart.views.blueprint)
    return None


def configure_logger(app):
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "User": user.models.User} # noqa

    app.shell_context_processor(shell_context)


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code: int = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code # noqa

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_commands(app):
    pass
