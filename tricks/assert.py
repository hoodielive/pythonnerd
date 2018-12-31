def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': 'Jordans', 'price': 14900}

apply_discount(shoes, 0.25)
