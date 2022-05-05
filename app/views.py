from datetime import datetime as dt
from sqlalchemy import extract
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
def births():
    if request.method == "GET":
        records = WikiData.query.all()
        current_date = dt.now().strftime("%d-%m")
        if len(records) == 0 or records.first().date[:5] != current_date:
            response = utils.get_api_data(utils.generate_endpoint(api_endpoints.ENDPOINTS.births))["births"]
            data = []
            for item in response:
                category = "births"
                page = item["pages"][0]
                extract = page["extract"]
                title = page["normalizedtitle"]
                link = page["content_urls"]["desktop"]["page"]
                date = current_date + "-" + str(item["year"])
                data.append(
                    WikiData(category = category, title = title, extract = extract, link = link, date = date)
                    )
            
            db.session.add_all(data)
            db.session.commit()
        
        records = WikiData.query.all()
        for item in records:
            print(item.date)
            print(item.title)
            print(item.link)
        
        return render_template("index.html")
