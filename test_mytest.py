# Филиппова Ирина, 27-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import body

def test_get_order_by_track():
    number = sender_stand_request.create_order()
    order_status_code = sender_stand_request.get_order(number)
    
    assert order_status_code == 200