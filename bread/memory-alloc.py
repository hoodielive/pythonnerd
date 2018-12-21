import csv 

def calculate_memory_expended(filename):
    '''
    Write strings into a tuple
    '''
    records = [] 
    rows = csv.reader(f)
    headings = next(f)
    with open(filename) as f:
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
        records = (route, date, daytype)  
    return records 

if __init__ == '__main__':
    import malloc 
    
