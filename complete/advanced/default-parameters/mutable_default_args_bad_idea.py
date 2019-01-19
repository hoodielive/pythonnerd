def create_account(name: str, holder: str, account_holders = None):
    # instead of account_holders: list = []
    if not account_holders:
        account_holders = []
    
    print(id(account_holders))
    account_holders.append(holder)
    print(id(account_holders))

    return {
            'name': name, 
            'main_account_holder': holder, 
            'account_holders': account_holders
    }

a1 = create_account('checking', 'Klaus')
a2 = create_account('savings', 'Rebekah')

print(a1); print(a2)
