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

def fetch_data(db_model):
    current_date = dt.now().strftime("%d-%m")
    records = db_model.query.all()
    data = []
    if len(records) == 0 or records[0].date[:5] != current_date:
        response = get_api_data(generate_endpoint(ENDPOINTS.births))["births"]
        for item in response:
            category = "BIRTH"
            page = item["pages"][0]
            extract = page["extract"]
            title = page["normalizedtitle"]
            link = page["content_urls"]["desktop"]["page"]
            date = current_date
            try:
                year = item["year"]
                date = date + "-" + str(year)
            except:
                year = ""
            data.append(
                db_model(category = category, title = title, extract = extract, link = link, date = date)
                )
    return data
