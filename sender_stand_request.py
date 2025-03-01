import config
import body
import requests 

def create_order():
    neworder = requests.post(url=config.URL_BASE + config.URL_CREATE_ORDER, json = body.body_create_order).json()["track"]
    print("Номер трека: ", neworder)
    return neworder

def get_order(number):
    order_info = requests.get(url=config.URL_BASE + config.URL_GET_ORDER + str(number))
    return order_info.status_code