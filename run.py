from app import create_app, db
from app.models import WikiData
from app.helpers import utils
from datetime import datetime as dt

app = create_app()
app.url_map.strict_slashes = False

if __name__ == "__main__":
    with app.app_context():
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
    app.run(debug = True)
