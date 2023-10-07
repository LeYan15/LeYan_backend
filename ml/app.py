import requests
import os
import logging
from http import HTTPStatus
from datetime import date, timedelta

from model import forecast
from config import settings

api_port = os.environ.get("API_PORT", "8000")
api_host = os.environ.get("API_PORT", "localhost")

_logger = logging.getLogger(__name__)


def setup_logging():
    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)
    handler_m = logging.StreamHandler()
    formatter_m = logging.Formatter(settings.FORMAT)
    handler_m.setFormatter(formatter_m)
    _logger.addHandler(handler_m)


def get_address(resource):
    return "http://" + api_host + ":" + api_port + "/" + resource


def get_stores():
    stores_url = get_address(settings.URL_STORES)
    resp = requests.get(stores_url)
    if resp.status_code != 200:
        _logger.warning("Could not get stores list")
        return []
    return resp.json()["data"]


def get_sales(store=None, sku=None):
    sale_url = get_address(settings.URL_SALES)
    params = {}
    if store is not None:
        params["store"] = store
    if sku is not None:
        params["sku"] = sku
    resp = requests.get(sale_url, params=params)
    if resp.status_code != HTTPStatus.OK:
        _logger.warning("Could not get sales history")
        return []
    return resp.json()["data"]


def get_categs_info():
    categs_url = get_address(settings.URL_CATEGORIES)
    resp = requests.get(categs_url)
    if resp.status_code != HTTPStatus.OK:
        _logger.warning("Could not get category info")
        return {}
    return {el["sku"]: el for el in resp.json()["data"]}


def main(today=date.today()):
    forecast_dates = [today + timedelta(days=d) for d in range(1, 6)]
    forecast_dates = [el.strftime(settings.DATA) for el in forecast_dates]
    categs_info = get_categs_info()
    for store in get_stores():
        result = []
        for item in get_sales(store=store["store"]):
            item_info = categs_info[item["sku"]]
            sales = item["fact"]
            prediction = forecast(sales, item_info, store)
            result.append(
                {
                    "store": store["store"],
                    "forecast_date": today.strftime(settings.DATA),
                    "forecast": {
                        "sku": item["sku"],
                        "sales_units": {
                            k: v for k, v in zip(forecast_dates, prediction)
                        },
                    },
                }
            )
        requests.post(
            get_address(settings.URL_FORECAST), json={"data": result}
        )


if __name__ == "__main__":
    setup_logging()
    main()