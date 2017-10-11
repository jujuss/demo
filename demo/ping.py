# encoding: utf-8

import logging

from flask import Blueprint

from deco import (
    log_deco,
    api_deco,
)

logger = logging.getLogger(__name__)
bp = Blueprint("ping", __name__)


@bp.route('')
@log_deco
@api_deco
def ping():
    return "pong"
