from datetime import datetime as dt
from . import db
from .models import *
from .helpers import utils, api_endpoints
from flask import Blueprint, redirect, render_template, request

views = Blueprint("views", __name__)

@views.route('/', methods = ['GET'])
def home():
    if request.method == "GET":
        return redirect("/births")

@views.route('/births', methods = ['GET'])
@views.route('/births/<int:page>', methods = ['GET'])
def births(page = 1):
    page = page
    per_page = 10
    if request.method == "GET":
        data = utils.fetch_data(WikiData)
        db.session.add_all(data)
        db.session.commit()
        
        records = WikiData.query.paginate(page, per_page, error_out = False)
        # for item in records:
        #     print(item.date)
        #     print(item.title)
        #     print(item.link)
        
        return render_template("index.html", records = records)
