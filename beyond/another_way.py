# export PYTHONPATH=not_searched

import sys 
[p for p in sys.path if 'not_searched' in p]

import path_test

path_test.found()
