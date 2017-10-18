from flask import flask


def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    # app.config.from_object(config)
    
    # Default root route.
    @app.route('/')
    def index():
        return 'Splash page'

    return app
