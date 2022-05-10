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
@views.route('/births/<int:page>', methods = ['GET'], strict_slashes = False)
def births(page = 1):
    page = page
    per_page = 10
    if request.method == "GET":
        records = WikiData.query.all()
        current_date = dt.now().strftime("%d-%m")
        if len(records) == 0 or records[0].date[:5] != current_date:
            if records[0].date[:5] != current_date:
                for record in records:
                    db.session.delete(record)
                db.session.commit()
            data = utils.fetch_data(WikiData, current_date)
            db.session.add_all(data)
            db.session.commit()
            
        records = WikiData.query.paginate(page, per_page, error_out = False)
        # for item in records:
        #     print(item.date)
        #     print(item.title)
        #     print(item.link)
        
        return render_template("index.html", records = records)
