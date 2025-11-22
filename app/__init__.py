import logging
from flask import Flask
from pythonjsonlogger import jsonlogger
from prometheus_flask_exporter import PrometheusMetrics

from .config import Config

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config())

    # Configure Structured Logging
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    logHandler.setFormatter(formatter)
    app.logger.addHandler(logHandler)
    app.logger.setLevel(logging.INFO)

    # Initialize Prometheus Metrics
    metrics = PrometheusMetrics(app)
    metrics.info('app_info', 'Application info', version='1.0.0')

    # Lazy imports to avoid circular deps during app init
    from .routes.health import bp as health_bp
    from .routes.loans import bp as loans_bp
    from .routes.stats import bp as stats_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(loans_bp, url_prefix="/api")
    app.register_blueprint(stats_bp, url_prefix="/api")

    return app
