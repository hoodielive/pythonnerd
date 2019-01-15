def save_to_file(content, filename):
    with open(filename, 'wt') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'rt') as file:
        return file.read() 
