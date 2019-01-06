# templates were added in PEP 292 and intended as an alternative to the built-in interpolation syntax [string.Template] 
import string

values = {'sing': 'lala'}

# Note the trigger is escaped by repeating the character twice
t = string.Template(""" 
    Variable            : $sing
    Escape              : $$ 
    Variable in text    : ${sing}ible
""")

print('TEMPLATE:', t.substitute(values))

# Note the trigger is escaped by repeating the character twice
s = """
    Variable            : %(sing)s 
    Escape              : %%
    Variable in text    : %(sing)siable
    """
print('INTERPOLATION:', s % values)

# Note the trigger is escaped by repeating the character twice
f = """
    Variable            : {sing}
    Escape              : {{}}
    Variable in text    : {sing}iable
    """

print('FORMAT:', s.format(**values))
