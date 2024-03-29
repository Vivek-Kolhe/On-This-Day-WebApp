from . import db

class WikiData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(30))
    title = db.Column(db.String(300))
    extract = db.Column(db.String(8000))
    link = db.Column(db.String(1000))
    date = db.Column(db.String(15))
