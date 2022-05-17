from . import db
from .models import *
from .helpers import utils
from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, request, abort

views = Blueprint("views", __name__)

@views.route('/', methods = ['GET'])
def home():
    if request.method == "GET":
        return redirect("/births")

@views.route('/<string:category_>', methods = ['GET'])
@views.route('/<string:category_>/<int:page>', methods = ['GET'], strict_slashes = False)
def births(category_, page = 1):
    page = page
    per_page = 10
    if request.method == "GET":
        if category_ not in ["births", "deaths", "events", "holidays", "selected"]:
            abort(404)
        records = WikiData.query.all()
        current_date = dt.now().strftime("%d-%m")
        if len(records) == 0 or records[0].date[:5] != current_date:
            if len(records) != 0 and records[0].date[:5] != current_date:
                for record in records:
                    db.session.delete(record)
                db.session.commit()
            data = utils.fetch_data(WikiData, current_date)
            db.session.add_all(data)
            db.session.commit()
            
        records = WikiData.query.filter_by(category = category_.upper()[:-1] if category_ != "selected" else "SELECTED").paginate(page, per_page, True)
        
        return render_template("index.html", category = category_, records = records)
