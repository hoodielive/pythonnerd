# sorry but this shit is too ugly - hoist it in the __init__ 
# import reader.reader
import reader

reader.reader.__file__

r = reader.reader.Reader('reader/reader.py')

print(r.read())
