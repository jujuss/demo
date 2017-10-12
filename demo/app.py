# encoding: utf-8

import logging
import os

from flask import Flask

import log
from ping import bp as ping_bp

log.setup(os.environ.get("ENV", "dev"))
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello, world"

# register buleprints
app.register_blueprint(ping_bp, url_prefix='/ping')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
