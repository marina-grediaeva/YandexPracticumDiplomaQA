# Марина Гредяева, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import send_requests
import data


def test_diploma():
    track_number = send_requests.create_order(data.user_body)['track']
    find_order = send_requests.find_order_by_track(track_number)
    assert find_order.status_code == 200


