from flask import Blueprint

bp = Blueprint('adminbp', __name__)

from app.adminbp import views
