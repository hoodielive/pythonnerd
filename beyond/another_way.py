# export PYTHONPATH=not_searched
# http://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
# http://docs.python.org/3/library/sys.html#sys.path
import sys 

[p for p in sys.path if 'not_searched' in p]

import path_test

path_test.found()
