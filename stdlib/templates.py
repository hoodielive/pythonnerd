# templates were added in PEP 292 and intended as an alternative to the built-in interpolation syntax [string.Template] 
import string

values = {'sing': 'lala'}

t = string.Template(""" 
    Variable            : $sing
    Escape              : $$ 
    Variable in text    : ${sing}ible
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable            : %(sing)s 
Escape              : %%
Variable in Text    : %(sing)siable
"""
print('INTERPOLATION:', s % values)
