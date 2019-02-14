import html 

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                    name=name,
                    attrs=attr_str, 
                    value=html.escape(value))
    return element

# Example 

# Creates '<item size="large" quantity="6">Dope Builds</item>'
make_element('item', 'Dope Builds', size='large', quantity=6)

# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')


def any_args(*args, **kwargs):
    print(args) # a Tuple 
    print(kwargs) # a Dict

any_args('Palo, Vodun, Ifa, Santeria, Macumba, Candomble, Lucumi', title="bokor", employ="lwa", ifa="babalawo", palo="palero") 
