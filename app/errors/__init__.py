# this is in the blueprint package directory called errors
# this init file is the blueprint creation

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
