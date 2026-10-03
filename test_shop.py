from shop import Order
from shop import OrderService
from shop import CONFIG
import pytest
def test_order_normal():

    products = [
        {
            "name": "Teclado",
            "price": 800,
            "quantity": 1
        },
        {
             "name": "Mouse",
            "price": 300,
            "quantity": 1
        }
    ]

    order = Order(products)

    service = OrderService(CONFIG)

    order_processed = service.process_order(order)

    result = service.calculate_total(order)

    assert order_processed['payment']['status'] == 'approved'
    assert result["subtotal"] == 1100
    assert result["discount"] == 110
    assert result["tax"] == 158.4
    assert result["total"] == 1148.4
