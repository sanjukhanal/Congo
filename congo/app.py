from flask import Flask

from congo.views import base


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(base.bp)


def configure_logger(app):
    pass


def create_app(config_object="congo.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    # register_extensions(congo)
    register_blueprints(app)
    # configure_logger(congo)
    return app
