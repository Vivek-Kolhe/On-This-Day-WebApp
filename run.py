from app import create_app, db
from app.models import WikiData
from app.helpers import utils

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        data = utils.fetch_data(WikiData)
        db.session.add_all(data)
        db.session.commit()
    app.run(debug = True)
