import requests
from datetime import datetime as dt
from .api_endpoints import ENDPOINTS

def check_date(current_date):
    today = dt.now().strftime("%d-%m-%Y")
    if today != current_date:
        return False
    return True

def get_api_data(api_endpoint):
    response = requests.get(api_endpoint, headers = {"content-type": "application/json"})
    if response.status_code == 200:
        return response.json()
    return None

def fetch_new_date():
    pass