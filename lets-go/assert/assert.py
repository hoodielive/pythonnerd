def applydiscount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price 

shoes = {
    "name": "fun shoes", 
    "price": 14900
}
applydiscount(shoes, 0.25)
