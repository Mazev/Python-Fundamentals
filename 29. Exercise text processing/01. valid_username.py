username = input().split(', ')

valid_usernames = []
for name in username:
    if 3 <= len(name) <= 16:
        if '-' in name or '_' in name or name.isalnum():
            valid_usernames.append(name)

for name in valid_usernames:
    print(name)