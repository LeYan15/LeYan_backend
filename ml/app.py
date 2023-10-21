import logging
import os
from datetime import date, timedelta
from http import HTTPStatus

import requests
from config import settings
from model import forecast

api_port = os.environ.get("API_PORT", "8000")
api_host = os.environ.get("API_HOST", "127.0.0.1")

_logger = logging.getLogger(__name__)


def setup_logging():
    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)
    handler_m = logging.StreamHandler()
    formatter_m = logging.Formatter(settings.FORMAT)
    handler_m.setFormatter(formatter_m)
    _logger.addHandler(handler_m)


def get_address(resource):
    return f"http://{api_host}:{api_port}/api/{resource}"


def get_shops():
    shops_url = get_address(settings.URL_SHOPS)
    resp = requests.get(shops_url)
    if resp.status_code != HTTPStatus.OK:
        _logger.warning("Could not get shops list")
        return []
    return resp.json()["results"]


def get_sales(shop=None, sku=None):
    sale_url = get_address(settings.URL_SALES)
    params = {}
    if shop is not None:
        params["name"] = shop
    if sku is not None:
        params["sku"] = sku
    resp = requests.get(sale_url, params=params)
    if resp.status_code != HTTPStatus.OK:
        _logger.warning("Could not get sales history")
        return []
    return resp.json()["data"]


def get_product_info():
    categs_url = get_address(settings.URL_CATEGORIES)
    resp = requests.get(categs_url)
    if resp.status_code != HTTPStatus.OK:
        _logger.warning("Could not get category info")
        return {}
    return {el["sku"]: el for el in resp.json()["data"]}


def main(today=date.today()):
    forecast_dates = [today + timedelta(days=d) for d in range(1, 14)]
    forecast_dates = [el.strftime(settings.DATA) for el in forecast_dates]
    categs_info = get_product_info()
    for shop in get_shops():
        result = []
        for item in get_sales(shop=shop["name"]):
            item_info = categs_info[item["sku"]]
            sales = item["fact"]
            prediction = forecast(sales, item_info, shop)
            result.append(
                {
                    "shop": shop["shop"],
                    "forecast_date": today.strftime(settings.DATA),
                    "forecast": {
                        "sku": item["sku"],
                        "sales_units": {
                            k: v for k, v in zip(forecast_dates, prediction)
                        },
                    },
                }
            )
        requests.post(get_address(settings.URL_FORECAST), json={"data": result})


if __name__ == "__main__":
    setup_logging()
    main()
