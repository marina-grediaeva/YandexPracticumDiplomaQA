# Марина Гредяева, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
#import data

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         params=body).json()

#track_number = create_order(data.user_body)['track']
#print(track_number)

def find_order_by_track(body):
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER,
                        params={'t': body})
#response = find_order_by_track(track_number)
#print(response.status_code)
#print(response.json())