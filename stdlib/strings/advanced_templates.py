# default syntax can be changed by adjusting the regular expression patterns it uses to find the variable names in
# the template body.

import string 

class TheTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
    Delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notunderscored
'''

d = {
        'with_underscore': 'replaced', 
        'notunderscored': 'not replaced'
}

t = TheTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
