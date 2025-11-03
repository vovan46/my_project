with open('new.txt', 'r', encoding='utf-8') as file:
    users = {}
    for line in file:
        if not line:
            continue
        parts = line.split('"')
        name = parts[1] 
        schet = parts[2].strip()
        acc, itog = schet.split(':')
        account = int(acc.replace('-', '').strip())
        itog_str = itog.strip()
        if itog_str[0] == '+':
            itog1 = float(itog_str[1:])
        else:  
            itog1 = -float(itog_str[1:])
        if name not in users:
            users[name] = {}
        if account not in users[name]:
            users[name][account] = 0.0    
        users[name][account] += itog1
for name, accounts in users.items():
    accounts_list = []
    for account, itog1 in sorted(accounts.items()):
        accounts_list.append(f"{account}: {itog1}")
    accounts_str = ", ".join(accounts_list)
    print(f'"{name}" - {accounts_str}')