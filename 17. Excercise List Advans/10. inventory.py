collecting_items = input().split(', ')

data = input()
while not data == 'Craft!':
    command, items = data.split(' - ')
    if command == 'Collect':
        if items not in collecting_items:
            collecting_items.append(items)
            if items in collecting_items:
                continue
    elif command == 'Drop':
        if items in collecting_items:
            collecting_items.remove(items)
    elif command == 'Combine Items':
        items = items.split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in collecting_items:
            index_old_item = collecting_items.index(old_item)
            index_new_item = index_old_item + 1
            collecting_items.insert(index_new_item, new_item)
    elif command == 'Renew':
        if items in collecting_items:
            collecting_items.remove(items)
            collecting_items.append(items)


    data = input()

print(', '.join(collecting_items))
