from . import db
from .models import *
from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route('/', methods = ['GET'])
def home():
    if request.method == "GET":
        add = BIRTHS(title = "Princess Charlotte of Cambridge", extract = "Princess Charlotte of Cambridge is a member of the British royal family. She is the second child and only daughter of Prince William, Duke of Cambridge, and Catherine, Duchess of Cambridge. She is fourth in the line of succession to the British throne.", link = "https://en.wikipedia.org/wiki/Princess_Charlotte_of_Cambridge", date = "05-02-2015")
        db.session.add(add)
        db.session.commit()
        record = BIRTHS.query.first()
        print(record.title)
        print(record.extract)
        print(record.link)
        print(record.date)
        return render_template("index.html")
