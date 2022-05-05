import requests
from datetime import datetime as dt
from .api_endpoints import ENDPOINTS

def generate_endpoint(api_endpoint):
    return api_endpoint + dt.now().strftime("/%m/%d")

def get_api_data(api_endpoint):
    response = requests.get(api_endpoint, headers = {"content-type": "application/json"})
    if response.status_code == 200:
        return response.json()
    return None

def check_empty_db(db_model):
    records = db_model.query.all()
    if len(records) == 0:
        return True
    return False

def check_date(current_date):
    today = dt.now().strftime("%d-%m")
    if today != current_date:
        return False
    return True
