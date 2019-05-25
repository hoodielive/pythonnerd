def get_unique_emails(file_name):
    """
    Read the file data and get all unique emails.
    """
    emails = set() 
    with open(file_name) as fread: 
        for line in fread: 
            match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
            for email in match:
                emails.add(email)
    return emails

get_unique_emails()
