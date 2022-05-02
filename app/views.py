from . import db
from .models import *
from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route('/', methods = ['GET'])
def home():
    if request.method == "GET":
        return render_template("index.html")