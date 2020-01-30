TAX_RATES_BY_STATE = {
    'MI': 1.06
}

def add_sales_tax(total, state):
    return total * TAX_RATES_BY_STATE[state]


add_sales_tax(93.2, 'Florida')
