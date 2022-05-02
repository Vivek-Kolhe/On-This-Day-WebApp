from . import db

class BIRTHS(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(300))
    extract = db.Column(db.String(8000))
    link = db.Column(db.String(1000))
    date = db.Column(db.String(15))

# class DEATHS(db.Model):
#     pass

# class EVENTS(db.Model):
#     pass

# class HOLIDAYS(db.Model):
#     pass

# class SELECTED(db.Model):
#     pass
